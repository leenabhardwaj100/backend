import { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Flower2, Info, ChevronRight, Activity, Beaker, CheckCircle2 } from 'lucide-react';

interface Prediction {
  prediction: string;
  confidence: number;
}

export default function App() {
  const [formData, setFormData] = useState({
    sepal_length: 5.1,
    sepal_width: 3.5,
    petal_length: 1.4,
    petal_width: 0.2
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Prediction | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      // In a real deployment, the backend would be serving on the same origin or /api
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to get prediction from server');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: parseFloat(value) || 0
    }));
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-8">
        {/* Header */}
        <header className="flex items-center space-x-4">
          <div className="p-3 bg-indigo-600 rounded-2xl shadow-lg shadow-indigo-200">
            <Flower2 className="w-8 h-8 text-white" />
          </div>
          <div>
            <h1 className="text-3xl font-bold tracking-tight text-slate-900">Iris Predictor Pro</h1>
            <p className="text-slate-500">Machine learning powered species classification</p>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Form Side */}
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="bg-white p-8 rounded-3xl shadow-sm border border-slate-200"
          >
            <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
              <Activity className="w-5 h-5 text-indigo-500" />
              Input Dimensions
            </h2>
            <form onSubmit={handleSubmit} className="space-y-6">
              {[
                { label: 'Sepal Length (cm)', name: 'sepal_length' },
                { label: 'Sepal Width (cm)', name: 'sepal_width' },
                { label: 'Petal Length (cm)', name: 'petal_length' },
                { label: 'Petal Width (cm)', name: 'petal_width' },
              ].map((field) => (
                <div key={field.name} className="space-y-2">
                  <label className="text-sm font-medium text-slate-600">{field.label}</label>
                  <input
                    type="number"
                    step="0.1"
                    name={field.name}
                    value={formData[field.name as keyof typeof formData]}
                    onChange={handleChange}
                    className="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all outline-none"
                    required
                  />
                </div>
              ))}
              <button
                type="submit"
                disabled={loading}
                className="w-full py-4 bg-indigo-600 text-white font-bold rounded-xl shadow-lg shadow-indigo-100 hover:bg-indigo-700 active:scale-95 transition-all flex items-center justify-center gap-2 disabled:opacity-50"
              >
                {loading ? (
                  <div className="w-6 h-6 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                ) : (
                  <>
                    Run Prediction
                    <ChevronRight className="w-5 h-5" />
                  </>
                )}
              </button>
            </form>
          </motion.div>

          {/* Result Side */}
          <div className="space-y-6">
            <AnimatePresence mode="wait">
              {result ? (
                <motion.div
                  key="result"
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  className="bg-indigo-600 text-white p-8 rounded-3xl shadow-xl space-y-6"
                >
                  <div className="flex justify-between items-start">
                    <span className="px-3 py-1 bg-white/20 rounded-full text-xs font-semibold tracking-wider uppercase">
                      Classification Result
                    </span>
                    <CheckCircle2 className="w-6 h-6 text-indigo-200" />
                  </div>
                  
                  <div>
                    <h3 className="text-4xl font-black capitalize">{result.prediction}</h3>
                    <p className="text-indigo-100 mt-2">Predicted Species</p>
                  </div>

                  <div className="pt-6 border-t border-white/10">
                    <div className="flex justify-between items-end mb-2">
                      <span className="text-sm text-indigo-100 font-medium whitespace-nowrap">Prediction Confidence</span>
                      <span className="text-2xl font-bold">{(result.confidence * 100).toFixed(1)}%</span>
                    </div>
                    <div className="w-full h-3 bg-white/10 rounded-full overflow-hidden">
                      <motion.div 
                        initial={{ width: 0 }}
                        animate={{ width: `${result.confidence * 100}%` }}
                        className="h-full bg-white rounded-full shadow-sm"
                      />
                    </div>
                  </div>
                </motion.div>
              ) : (
                <motion.div
                  key="placeholder"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  className="bg-slate-200/50 border-2 border-dashed border-slate-300 h-full min-h-[400px] rounded-3xl flex flex-col items-center justify-center text-slate-400 p-8 text-center space-y-4"
                >
                  <Beaker className="w-12 h-12" />
                  <div>
                    <h3 className="text-lg font-semibold text-slate-500">Ready to Analyze</h3>
                    <p className="text-sm max-w-[200px] mx-auto">Fill in the dimensions and run the model to see your results.</p>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            {error && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="p-4 bg-red-50 border border-red-100 text-red-600 rounded-2xl flex items-start gap-3"
              >
                <Info className="w-5 h-5 shrink-0 mt-0.5" />
                <p className="text-sm font-medium">{error}</p>
              </motion.div>
            )}

            <div className="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 space-y-4">
              <h4 className="font-semibold text-slate-800 flex items-center gap-2">
                <Info className="w-4 h-4 text-slate-400" />
                Technical Details
              </h4>
              <ul className="text-xs text-slate-500 space-y-2">
                <li>• Algorithm: Scikit-learn Random Forest Classifier</li>
                <li>• Dataset: Fisher's Iris Data (150 samples)</li>
                <li>• Features: Sepal & Petal dimensions</li>
                <li>• Accuracy: ~96.7%</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

