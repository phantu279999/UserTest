import React, { useState, useEffect, useCallback } from 'react';
import { ActionType } from './types';
import type { AppState, ActionItem, TestCase } from './types';
import { DEFAULT_TEST_CASE, INITIAL_JSON_EXAMPLE } from './constants';
import ActionItemEditor from './components/ActionItemEditor';
import JsonPreview from './components/JsonPreview';
import {
  Plus, Code2, Download, Wand2, Settings,
  Trash2, Loader2, AlertTriangle, Menu, Pencil, Check, X
} from 'lucide-react';

const App = () => {
  const [state, setState] = useState<AppState>(() => {
    // Transform initial example to internal state format
    const { run, ...rest } = INITIAL_JSON_EXAMPLE;
    return {
      run: run as string[],
      testCases: rest as Record<string, TestCase>
    };
  });

  const [activeTest, setActiveTest] = useState<string>(state.run[0] || '');
  const [isAiModalOpen, setIsAiModalOpen] = useState(false);
  const [aiPrompt, setAiPrompt] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [generationError, setGenerationError] = useState<string | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(true);

  // Renaming State
  const [isRenaming, setIsRenaming] = useState(false);
  const [renameValue, setRenameValue] = useState('');

  // Derived state: Full Config Object for JSON Preview
  const fullConfig = React.useMemo(() => {
    return {
      run: state.run,
      ...state.testCases
    };
  }, [state]);

  // Handlers for Test Case Management
  const addTestCase = (name: string = `test_case_${Date.now()}`) => {
    if (state.testCases[name]) return; // Prevent duplicates
    setState(prev => ({
      ...prev,
      testCases: { ...prev.testCases, [name]: { ...DEFAULT_TEST_CASE } }
    }));
    setActiveTest(name);
  };

  const removeTestCase = (name: string) => {
    if (!window.confirm(`Delete "${name}"?`)) return;
    setState(prev => {
      const newCases = { ...prev.testCases };
      delete newCases[name];
      const newRun = prev.run.filter(t => t !== name);
      return { run: newRun, testCases: newCases };
    });
    if (activeTest === name) setActiveTest('');
  };

  const toggleRunStatus = (name: string) => {
    setState(prev => {
      const isRunning = prev.run.includes(name);
      return {
        ...prev,
        run: isRunning ? prev.run.filter(t => t !== name) : [...prev.run, name]
      };
    });
  };

  const startRenaming = () => {
    if (!activeTest) return;
    setRenameValue(activeTest);
    setIsRenaming(true);
  };

  const saveRename = () => {
    const trimmedName = renameValue.trim();
    if (!trimmedName) {
      setIsRenaming(false);
      return;
    }

    if (trimmedName === activeTest) {
      setIsRenaming(false);
      return;
    }

    if (state.testCases[trimmedName]) {
      alert(`Test case "${trimmedName}" already exists.`);
      return;
    }

    setState(prev => {
      // Create new object preserving order
      const newTestCases: Record<string, TestCase> = {};
      Object.keys(prev.testCases).forEach(key => {
        if (key === activeTest) {
          newTestCases[trimmedName] = prev.testCases[key];
        } else {
          newTestCases[key] = prev.testCases[key];
        }
      });

      const newRun = prev.run.map(item => item === activeTest ? trimmedName : item);

      return {
        run: newRun,
        testCases: newTestCases
      };
    });

    setActiveTest(trimmedName);
    setIsRenaming(false);
  };

  const updateTestCaseConfig = (field: keyof TestCase, value: any) => {
    if (!activeTest) return;
    setState(prev => ({
      ...prev,
      testCases: {
        ...prev.testCases,
        [activeTest]: {
          ...prev.testCases[activeTest],
          [field]: value
        }
      }
    }));
  };

  // Handlers for Actions within a Test Case
  const updateAction = useCallback((index: number, updatedAction: ActionItem) => {
    setState(prev => {
      const currentCase = prev.testCases[activeTest];
      if (!currentCase) return prev;

      const newActions = [...currentCase.action];
      newActions[index] = updatedAction;

      return {
        ...prev,
        testCases: {
          ...prev.testCases,
          [activeTest]: { ...currentCase, action: newActions }
        }
      };
    });
  }, [activeTest]);

  const addAction = () => {
    if (!activeTest) return;
    const newAction: ActionItem = { type: ActionType.CLICK, locator: '', value: '' };
    setState(prev => ({
      ...prev,
      testCases: {
        ...prev.testCases,
        [activeTest]: {
          ...prev.testCases[activeTest],
          action: [...prev.testCases[activeTest].action, newAction]
        }
      }
    }));
  };

  const removeAction = (index: number) => {
    setState(prev => {
      const currentCase = prev.testCases[activeTest];
      if (!currentCase) return prev;
      const newActions = currentCase.action.filter((_, i) => i !== index);
      return {
        ...prev,
        testCases: {
          ...prev.testCases,
          [activeTest]: { ...currentCase, action: newActions }
        }
      };
    });
  };

  const moveAction = (index: number, direction: 'up' | 'down') => {
    setState(prev => {
      const currentCase = prev.testCases[activeTest];
      const actions = [...currentCase.action];
      const targetIndex = direction === 'up' ? index - 1 : index + 1;

      if (targetIndex < 0 || targetIndex >= actions.length) return prev;

      [actions[index], actions[targetIndex]] = [actions[targetIndex], actions[index]];

      return {
        ...prev,
        testCases: {
          ...prev.testCases,
          [activeTest]: { ...currentCase, action: actions }
        }
      };
    });
  };


  return (
    <div className="flex h-screen bg-slate-900 overflow-hidden">

      {/* Sidebar: Test Cases List */}
      <div className={`${sidebarOpen ? 'w-64' : 'w-0'} transition-all duration-300 bg-slate-900 border-r border-slate-700 flex flex-col shrink-0`}>
        <div className="p-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-lg text-blue-400">
            <Settings size={20} />
            <span className={`${!sidebarOpen && 'hidden'}`}>Test Suite</span>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-2">
          {Object.keys(state.testCases).map((key) => (
            <div
              key={key}
              onClick={() => setActiveTest(key)}
              className={`
                group flex items-center justify-between p-3 mb-2 rounded cursor-pointer border transition-all
                ${activeTest === key ? 'bg-blue-900/20 border-blue-500/50' : 'bg-slate-800/50 border-transparent hover:bg-slate-800'}
              `}
            >
              <div className="flex items-center gap-2 overflow-hidden">
                <input
                  type="checkbox"
                  checked={state.run.includes(key)}
                  onChange={(e) => { e.stopPropagation(); toggleRunStatus(key); }}
                  className="rounded border-slate-600 bg-slate-700 text-blue-500 focus:ring-offset-slate-900 shrink-0"
                  title="Include in RUN list"
                />
                <span className={`text-sm truncate ${activeTest === key ? 'text-blue-100' : 'text-slate-400'}`}>{key}</span>
              </div>
              <button
                onClick={(e) => { e.stopPropagation(); removeTestCase(key); }}
                className="opacity-0 group-hover:opacity-100 text-slate-500 hover:text-red-400 transition-opacity"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>

        <div className="p-4 border-t border-slate-800">
          <button
            onClick={() => addTestCase()}
            className="w-full flex items-center justify-center gap-2 py-2 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-sm transition-colors border border-slate-700"
          >
            <Plus size={16} /> New Test Case
          </button>

          <button
            onClick={() => setIsAiModalOpen(true)}
            className="mt-3 w-full flex items-center justify-center gap-2 py-2 px-4 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 text-white rounded text-sm transition-all shadow-lg shadow-purple-900/20"
          >
            <Wand2 size={16} /> AI Gen
          </button>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col h-full min-w-0">

        {/* Header / Toolbar */}
        <header className="h-16 bg-slate-900 border-b border-slate-700 flex items-center justify-between px-6 shadow-sm z-10 shrink-0">
          <div className="flex items-center gap-4 flex-1">
            <button onClick={() => setSidebarOpen(!sidebarOpen)} className="text-slate-400 hover:text-slate-100">
               <Menu size={20} />
            </button>

            {activeTest ? (
               isRenaming ? (
                 <div className="flex items-center gap-2 bg-slate-800 p-1 rounded border border-slate-600">
                   <input
                      type="text"
                      className="bg-transparent text-slate-100 outline-none px-2 font-bold w-48 md:w-64"
                      value={renameValue}
                      onChange={(e) => setRenameValue(e.target.value)}
                      onKeyDown={(e) => e.key === 'Enter' && saveRename()}
                      autoFocus
                   />
                   <button onClick={saveRename} className="p-1 hover:bg-green-900/50 text-green-400 rounded"><Check size={16}/></button>
                   <button onClick={() => setIsRenaming(false)} className="p-1 hover:bg-red-900/50 text-red-400 rounded"><X size={16}/></button>
                 </div>
               ) : (
                  <div className="flex items-center gap-3 group">
                    <h1 className="text-xl font-bold text-slate-100 hidden md:block truncate max-w-[300px]" title={activeTest}>
                      {activeTest}
                    </h1>
                    <button
                      onClick={startRenaming}
                      className="text-slate-500 hover:text-blue-400 opacity-0 group-hover:opacity-100 transition-all"
                      title="Rename Test Case"
                    >
                      <Pencil size={16} />
                    </button>
                  </div>
               )
            ) : (
              <h1 className="text-xl font-bold text-slate-500">Select a Test Case</h1>
            )}

          </div>
          <div className="flex items-center gap-4 shrink-0">
             {activeTest && (
                <div className="flex items-center bg-slate-800 rounded px-3 py-1.5 border border-slate-700">
                  <span className="text-xs text-slate-500 mr-2 uppercase font-semibold hidden sm:inline">Global Sleep</span>
                  <input
                    type="number"
                    value={state.testCases[activeTest].time_sleep_action}
                    onChange={(e) => updateTestCaseConfig('time_sleep_action', parseInt(e.target.value) || 0)}
                    className="w-12 bg-transparent text-slate-200 text-sm text-center outline-none border-b border-slate-600 focus:border-blue-500"
                  />
                </div>
             )}
            <div className="h-8 w-px bg-slate-700 mx-2 hidden sm:block"></div>
            <a
               href={`data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(fullConfig, null, 2))}`}
               download="config.json"
               className="flex items-center gap-2 text-slate-400 hover:text-green-400 transition-colors text-sm"
            >
              <Download size={18} /> <span className="hidden sm:inline">Export</span>
            </a>
          </div>
        </header>

        {/* Content Split: Editor & Preview */}
        <div className="flex-1 flex flex-col lg:flex-row overflow-hidden relative">

          {/* Editor Area - with floating button */}
          <div className="flex-1 relative bg-slate-900 min-w-0 flex flex-col">
            <div className="flex-1 overflow-y-auto p-6 pb-24">
              {activeTest ? (
                <div className="max-w-8xl mx-auto">
                  <div className="flex items-center justify-between mb-6">
                    <h2 className="text-lg font-medium text-slate-300 flex items-center gap-2">
                      <Code2 size={20} className="text-blue-500" />
                      Actions Sequence
                    </h2>
                    <span className="text-xs text-slate-500 bg-slate-800 px-2 py-1 rounded-full">
                      {state.testCases[activeTest].action.length} steps
                    </span>
                  </div>

                  {state.testCases[activeTest].action.length === 0 ? (
                    <div className="text-center py-20 border-2 border-dashed border-slate-800 rounded-xl bg-slate-900/50">
                      <p className="text-slate-500 mb-4">No actions defined yet.</p>
                      <button onClick={addAction} className="text-blue-400 hover:underline">Add your first action</button>
                    </div>
                  ) : (
                    state.testCases[activeTest].action.map((action, idx) => (
                      <ActionItemEditor
                        key={idx}
                        index={idx}
                        action={action}
                        onChange={updateAction}
                        onRemove={removeAction}
                        onMoveUp={(i) => moveAction(i, 'up')}
                        onMoveDown={(i) => moveAction(i, 'down')}
                        isFirst={idx === 0}
                        isLast={idx === state.testCases[activeTest].action.length - 1}
                      />
                    ))
                  )}
                </div>
              ) : (
                 <div className="h-full flex flex-col items-center justify-center text-slate-600">
                    <Settings size={48} className="mb-4 opacity-20" />
                    <p>Select or create a test case to begin editing.</p>
                 </div>
              )}
            </div>

            {/* Floating Action Button */}
            {activeTest && (
              <div className="absolute bottom-8 right-8 z-20">
                 <button
                  onClick={addAction}
                  className="flex items-center justify-center w-14 h-14 bg-blue-600 hover:bg-blue-500 text-white rounded-full shadow-lg shadow-blue-900/40 transition-all hover:scale-105"
                  title="Add Action"
                >
                  <Plus size={28} />
                </button>
              </div>
            )}
          </div>

          {/* JSON Preview Panel */}
          <div className="hidden lg:block w-[400px] border-l border-slate-700 bg-[#1e1e1e] p-4 overflow-hidden shrink-0">
            <JsonPreview data={fullConfig} />
          </div>
        </div>
      </div>

      {/* AI Modal */}
      {isAiModalOpen && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-slate-800 rounded-xl border border-slate-700 shadow-2xl w-full max-w-lg p-6 relative">
             <button
                onClick={() => setIsAiModalOpen(false)}
                className="absolute top-4 right-4 text-slate-500 hover:text-white"
             >
               <Plus size={24} className="rotate-45" />
             </button>

             <div className="flex items-center gap-3 mb-4 text-purple-400">
                <Wand2 size={24} />
                <h2 className="text-xl font-bold text-white">Generate Test Case</h2>
             </div>

             <p className="text-slate-400 text-sm mb-4">
               Describe the test flow in natural language. The AI will generate the actions, locators, and verification steps for you.
             </p>

             <textarea
               className="w-full h-32 bg-slate-900 border border-slate-700 rounded-lg p-3 text-slate-200 focus:ring-2 focus:ring-purple-500 outline-none resize-none mb-4"
               placeholder="e.g., Navigate to 'example.com', enter 'user123' into the username field, click login, and verify the dashboard title says 'Welcome'."
               value={aiPrompt}
               onChange={(e) => setAiPrompt(e.target.value)}
             ></textarea>

             {generationError && (
               <div className="mb-4 p-3 bg-red-900/20 border border-red-900/50 rounded flex items-center gap-2 text-red-400 text-sm">
                 <AlertTriangle size={16} />
                 {generationError}
               </div>
             )}

             <div className="flex justify-end gap-3">
               <button
                 onClick={() => setIsAiModalOpen(false)}
                 className="px-4 py-2 text-slate-400 hover:text-white transition-colors"
                 disabled={isGenerating}
               >
                 Cancel
               </button>
               <button
                 disabled={isGenerating || !aiPrompt.trim()}
                 className="px-6 py-2 bg-purple-600 hover:bg-purple-500 text-white rounded-lg font-medium flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
               >
                 {isGenerating ? <Loader2 size={18} className="animate-spin" /> : <Wand2 size={18} />}
                 {isGenerating ? 'Generating...' : 'Generate'}
               </button>
             </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;