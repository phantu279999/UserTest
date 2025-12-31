import React from 'react';
import { ActionType, LocatorType, ResultType } from '../types';
import type { ActionItem, ActionResult } from '../types';
import { ACTION_TYPES, LOCATOR_TYPES, RESULT_TYPES } from '../constants';
import { Trash2, Plus, ChevronDown, ChevronUp, AlertCircle } from 'lucide-react';

interface Props {
  action: ActionItem;
  index: number;
  onChange: (index: number, updated: ActionItem) => void;
  onRemove: (index: number) => void;
  onMoveUp: (index: number) => void;
  onMoveDown: (index: number) => void;
  isFirst: boolean;
  isLast: boolean;
}

const ActionItemEditor: React.FC<Props> = ({
  action, index, onChange, onRemove, onMoveUp, onMoveDown, isFirst, isLast
}) => {

  const handleChange = (field: keyof ActionItem, value: any) => {
    onChange(index, { ...action, [field]: value });
  };

  const handleResultChange = (field: keyof ActionResult, value: any) => {
    const currentResult = action.result || { type: ResultType.DISPLAY };
    const updatedResult = { ...currentResult, [field]: value };
    // cleanup empty result fields if needed, but for now we keep structure
    onChange(index, { ...action, result: updatedResult });
  };

  const toggleResult = () => {
    if (action.result) {
      const { result, ...rest } = action;
      onChange(index, rest);
    } else {
      onChange(index, { ...action, result: { type: ResultType.XPATH_TEXT, value: '', xpath: '' } });
    }
  };

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-lg p-4 mb-3 shadow-sm hover:border-slate-600 transition-colors">
      <div className="flex justify-between items-start mb-3">
        <div className="flex items-center gap-2">
          <span className="bg-slate-700 text-slate-300 text-xs font-mono px-2 py-1 rounded">#{index + 1}</span>
          <input
            type="text"
            placeholder="Action Name (Optional)"
            className="bg-transparent border-b border-slate-600 focus:border-blue-500 outline-none text-sm text-slate-200 w-48"
            value={action.name || ''}
            onChange={(e) => handleChange('name', e.target.value)}
          />
        </div>
        <div className="flex gap-1">
           <button
            onClick={() => onMoveUp(index)}
            disabled={isFirst}
            className="p-1 hover:bg-slate-700 rounded disabled:opacity-30 text-slate-400"
          >
            <ChevronUp size={16} />
          </button>
          <button
            onClick={() => onMoveDown(index)}
            disabled={isLast}
            className="p-1 hover:bg-slate-700 rounded disabled:opacity-30 text-slate-400"
          >
            <ChevronDown size={16} />
          </button>
          <button
            onClick={() => onRemove(index)}
            className="p-1 hover:bg-red-900/50 text-red-400 rounded ml-2"
          >
            <Trash2 size={16} />
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-12 gap-3 mb-2">
        {/* Action Type */}
        <div className="md:col-span-3">
          <label className="block text-xs text-slate-500 mb-1">Action Type</label>
          <select
            className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1.5 text-sm text-slate-200 focus:ring-1 focus:ring-blue-500 outline-none"
            value={action.type}
            onChange={(e) => handleChange('type', e.target.value)}
          >
            {ACTION_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
          </select>
        </div>

        {/* Locator Type */}
        {action.type !== ActionType.GET_DOMAIN && (
           <div className="md:col-span-3">
            <label className="block text-xs text-slate-500 mb-1">Locator Type</label>
            <select
              className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1.5 text-sm text-slate-200 focus:ring-1 focus:ring-blue-500 outline-none"
              value={action.locator_type || LocatorType.XPATH}
              onChange={(e) => handleChange('locator_type', e.target.value)}
            >
              {LOCATOR_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
            </select>
          </div>
        )}

        {/* Locator Value */}
        {action.type !== ActionType.GET_DOMAIN && (
          <div className="md:col-span-6">
            <label className="block text-xs text-slate-500 mb-1">Locator</label>
            <input
              type="text"
              className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1.5 text-sm text-slate-200 focus:ring-1 focus:ring-blue-500 outline-none font-mono"
              value={action.locator || ''}
              onChange={(e) => handleChange('locator', e.target.value)}
              placeholder="//div[@id='example']"
            />
          </div>
        )}

         {/* Value / URL */}
         <div className="md:col-span-9">
            <label className="block text-xs text-slate-500 mb-1">
              {action.type === ActionType.GET_DOMAIN ? 'URL / Domain' : 'Input Value'}
            </label>
            <input
              type="text"
              className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1.5 text-sm text-slate-200 focus:ring-1 focus:ring-blue-500 outline-none"
              value={action.value || ''}
              onChange={(e) => handleChange('value', e.target.value)}
              placeholder="Value..."
            />
          </div>

           {/* Sleep */}
          <div className="md:col-span-3">
            <label className="block text-xs text-slate-500 mb-1">Sleep (sec)</label>
            <input
              type="number"
              className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1.5 text-sm text-slate-200 focus:ring-1 focus:ring-blue-500 outline-none"
              value={action.sleep || ''}
              onChange={(e) => handleChange('sleep', parseFloat(e.target.value))}
              placeholder="0"
            />
          </div>
      </div>

      {/* Advanced / Drag Drop */}
      {action.type === ActionType.DRAG_AND_DROP && (
        <div className="bg-slate-900/50 p-2 rounded mb-2 border border-slate-700/50">
           <p className="text-xs text-slate-400 mb-2 font-semibold">Target Element (Drag To)</p>
           <div className="grid grid-cols-2 gap-2">
             <select
                className="bg-slate-800 border border-slate-700 rounded px-2 py-1 text-sm text-slate-300"
                value={action.locator_type_2 || LocatorType.XPATH}
                onChange={(e) => handleChange('locator_type_2', e.target.value)}
              >
                {LOCATOR_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
              </select>
              <input
                type="text"
                className="bg-slate-800 border border-slate-700 rounded px-2 py-1 text-sm text-slate-300 font-mono"
                value={action.locator_2 || ''}
                onChange={(e) => handleChange('locator_2', e.target.value)}
                placeholder="Target locator..."
              />
           </div>
        </div>
      )}

      {/* Verification Result Section */}
      <div className="mt-3 pt-2 border-t border-slate-700/50">
        <button
          onClick={toggleResult}
          className={`text-xs flex items-center gap-1 ${action.result ? 'text-blue-400' : 'text-slate-500 hover:text-slate-300'}`}
        >
          {action.result ? <ChevronDown size={12} /> : <Plus size={12} />}
          {action.result ? 'Verify Result' : 'Add Verification'}
        </button>

        {action.result && (
          <div className="mt-2 p-3 bg-blue-900/10 border border-blue-900/30 rounded grid grid-cols-1 md:grid-cols-3 gap-3">
             <div>
              <label className="block text-[10px] text-blue-300/70 mb-1 uppercase">Check Type</label>
              <select
                className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-slate-200"
                value={action.result.type}
                onChange={(e) => handleResultChange('type', e.target.value)}
              >
                {RESULT_TYPES.map(t => <option key={t} value={t}>{t}</option>)}
              </select>
            </div>
            <div className="md:col-span-2">
              <label className="block text-[10px] text-blue-300/70 mb-1 uppercase">Expected Value</label>
              <input
                type="text"
                className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-slate-200"
                value={action.result.value || ''}
                onChange={(e) => handleResultChange('value', e.target.value)}
              />
            </div>
            {(action.result.type === ResultType.XPATH || action.result.type === ResultType.XPATH_TEXT) && (
              <div className="md:col-span-3">
                 <label className="block text-[10px] text-blue-300/70 mb-1 uppercase">Validation XPath</label>
                <input
                  type="text"
                  className="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-slate-200 font-mono"
                  value={action.result.xpath || ''}
                  onChange={(e) => handleResultChange('xpath', e.target.value)}
                />
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default ActionItemEditor;