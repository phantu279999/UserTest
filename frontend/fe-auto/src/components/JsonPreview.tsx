import React from 'react';
import { Copy, Check } from 'lucide-react';

interface Props {
  data: any;
}

const JsonPreview: React.FC<Props> = ({ data }) => {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(JSON.stringify(data, null, 2));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex flex-col h-full bg-[#1e1e1e] text-slate-300 rounded-lg overflow-hidden border border-slate-700 shadow-xl">
      <div className="flex justify-between items-center px-4 py-2 bg-slate-800 border-b border-slate-700">
        <h3 className="text-sm font-semibold text-slate-200">config.json</h3>
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 text-xs bg-slate-700 hover:bg-slate-600 px-2 py-1 rounded transition-colors"
        >
          {copied ? <Check size={14} className="text-green-400"/> : <Copy size={14} />}
          {copied ? "Copied" : "Copy"}
        </button>
      </div>
      <div className="flex-1 overflow-auto p-4 font-mono text-xs md:text-sm">
        <pre className="whitespace-pre-wrap break-all text-green-400">
          {JSON.stringify(data, null, 2)}
        </pre>
      </div>
    </div>
  );
};

export default JsonPreview;