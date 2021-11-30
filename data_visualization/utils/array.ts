export function uniqueValues<T, U>(array: Array<U>, callback: (value: U) => T) {
    return Array.from(new Set(array.map(callback)))
}
