// types.ts
import { ProgressEvent } from 'web-workers-ts';

// Import type definitions from other modules
import { AnalyticsEvent } from './analytics-event';

// Define types for the analytics worker
type WorkerMessage = {
  type: 'handleEvent' | 'reportProgress' | 'exit';
  payload?: AnalyticsEvent | ProgressEvent | undefined;
};

type WorkerResponse = {
  type: 'processedEvent' | 'completed' | 'error';
  payload?: AnalyticsEvent | Error | undefined;
};

// Export the types
export { WorkerMessage, WorkerResponse };