export interface EnvQLOptions {
  schemaPath?: string;
  keyPath?: string;
}

export class EnvQLError extends Error {}

export function load<T = Record<string, any>>(options?: EnvQLOptions): T;
export function generateMasterKey(keyPath?: string): string;
export function loadMasterKey(keyPath?: string): string;
export function decryptFernet(tokenBase64: string, keyBase64: string): string;
export function encryptFernet(plainText: string, keyBase64: string): string;
