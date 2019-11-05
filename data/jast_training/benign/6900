var ElementExtensions = /** @class */ (function () {
    function ElementExtensions() {
    }
    ElementExtensions.width = function (item) {
        if (item) {
            if (item.nativeElement)
                return item.nativeElement.offsetWidth;
            return item.offsetWidth;
        }
        return 0;
    };
    ElementExtensions.height = function (item) {
        if (item) {
            if (item.nativeElement) {
                if (item.nativeElement.clientHeight == 0)
                    return item.nativeElement.offsetHeight;
                return item.nativeElement.clientHeight;
            }
            if (item.clientHeight == 0)
                return item.offsetHeight;
            return item.clientHeight;
        }
        return 0;
    };
    ElementExtensions.scrollWidth = function (item) {
        if (item) {
            if (item.nativeElement)
                return item.nativeElement.scrollWidth;
            return item.scrollWidth;
        }
        return 0;
    };
    ElementExtensions.scrollHeight = function (item) {
        if (item) {
            if (item.nativeElement)
                return item.nativeElement.scrollHeight;
            return item.scrollHeight;
        }
        return 0;
    };
    ElementExtensions.parsePx = function (item) {
        return parseInt(item, 10);
    };
    ElementExtensions.getParentScrollTop = function (item) {
        if (item) {
            if (item.scrollTop > 0)
                return item.scrollTop;
            return ElementExtensions.getParentScrollTop(item.parentElement);
        }
        return 0;
    };
    return ElementExtensions;
}());
export { ElementExtensions };
