// interface Array<T> {
//     findNextItem(item: any) : any;
// }
// Array.prototype.findNextItem = function(item: any): any {
//     this
//     if (!this || this.length == 0)
//         return undefined;
//     if (!item)
//         return this[0];
//     var index = this.indexOf(item);
//     if (index == -1 || index + 1 == this.length)
//         return undefined;
//     return this[index+1];
// }
var ArrayExtensions = /** @class */ (function () {
    function ArrayExtensions() {
    }
    ArrayExtensions.findNextItem = function (items, item) {
        if (!items || items.length == 0)
            return undefined;
        if (!item)
            return items[0];
        var index = items.indexOf(item);
        if (index == -1 || index + 1 == items.length)
            return undefined;
        return items[index + 1];
    };
    ArrayExtensions.findPreviousItem = function (items, item) {
        if (!items || items.length == 0)
            return undefined;
        if (!item)
            return items[0];
        var index = items.indexOf(item);
        if (index == -1 || index == 0)
            return undefined;
        return items[index - 1];
    };
    return ArrayExtensions;
}());
export { ArrayExtensions };
