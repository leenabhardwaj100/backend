import express from "express";
import { createServer as createViteServer } from "vite";
import path from "path";
import { spawn } from "child_process";
import { createProxyMiddleware } from "http-proxy-middleware";

async function startServer() {
  const app = express();
  const PORT = 3000;
  const PYTHON_PORT = 8000;

  console.log("Installing Python requirements...");
  try {
    const pipInstall = spawn("pip3", ["install", "-r", "requirements.txt"]);
    await new Promise((resolve) => pipInstall.on("close", resolve));
    console.log("Python requirements installation check complete.");
  } catch (err) {
    console.error("Failed to run pip install. Please ensure python3 and pip3 are installed.");
  }

  console.log("Starting Python FastAPI backend...");
  
  // Start the Python backend
  const pythonProcess = spawn("python3", [
    "-m", "uvicorn", 
    "app:app", 
    "--host", "127.0.0.1", 
    "--port", PYTHON_PORT.toString()
  ]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(`[Python] ${data}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`[Python Error] ${data}`);
  });

  pythonProcess.on("close", (code) => {
    console.log(`Python process exited with code ${code}`);
  });

  // Proxy /predict to FastAPI
  app.use(
    "/predict",
    createProxyMiddleware({
      target: `http://127.0.0.1:${PYTHON_PORT}`,
      changeOrigin: true,
    })
  );

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath));
    app.get('*', (req, res) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Main server running on http://localhost:${PORT}`);
    console.log(`Proxying /predict requests to Python backend on port ${PYTHON_PORT}`);
  });
}

startServer().catch((err) => {
  console.error("Failed to start server:", err);
});
