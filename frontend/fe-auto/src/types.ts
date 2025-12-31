export enum ActionType {
  GET_DOMAIN = 'get_domain',
  OPEN_NEW_TAB = 'open_new_tab',
  CLICK = 'click',
  INPUT = 'input',
  INPUT_ENTER = 'input_enter',
  ENTER = 'enter',
  SWITCH_TO_FRAME = 'switch_to_frame',
  SWITCH_TO_NEXT_TAB = 'switch_to_next_tab',
  SWITCH_TO_LAST_TAB = 'switch_to_last_tab',
  SWITCH_TO_FIRST_TAB = 'switch_to_first_tab',
  MOVE = 'move',
  MOVE_CLICK = 'move_click',
  DRAG_AND_DROP = 'drag_and_drop',
  CLEAR = 'clear',
  CLEAR_AND_INPUT = 'clear_and_input',
}

export enum LocatorType {
  XPATH = 'xpath',
  ID = 'id',
  LINK_TEXT = 'link text',
  PARTIAL_LINK_TEXT = 'partial link text',
  NAME = 'name',
  TAG_NAME = 'tag name',
  CLASS_NAME = 'class name',
  CSS_SELECTOR = 'css selector',
}

export enum ResultType {
  TITLE = 'title',
  XPATH = 'xpath',
  DISPLAY = 'display',
  XPATH_TEXT = 'xpath_text',
  URL = 'url',
  ALERT = 'alert',
  STATUS = 'status',
}

export interface ActionResult {
  type: ResultType | string; // Allow string for flexibility if enum misses something
  value?: string | number;
  xpath?: string;
}

export interface ActionItem {
  name?: string;
  type: ActionType | string;
  locator?: string;
  locator_type?: LocatorType | string;
  value?: string;
  sleep?: number;
  result?: ActionResult;
  // Second locator fields
  locator_2?: string;
  locator_type_2?: LocatorType | string;
}

export interface TestCase {
  time_sleep_action: number;
  action: ActionItem[];
}

// The root configuration object structure
export interface TestConfig {
  run: string[];
  [key: string]: TestCase | string[] | any; // Index signature to allow dynamic test case keys
}

// Helper type for our internal state management
export interface AppState {
  run: string[];
  testCases: Record<string, TestCase>;
}