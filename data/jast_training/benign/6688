var FlexBasisResizeModel = /** @class */ (function () {
    function FlexBasisResizeModel(element, IsPrevious, IsHorizontal) {
        this.IsPrevious = IsPrevious;
        this.IsHorizontal = IsHorizontal;
        if (element)
            this.Element = element.nativeElement ? element.nativeElement : element;
    }
    FlexBasisResizeModel.prototype.resize = function (event, movingEle) {
        if (!this.Element)
            return;
        if (event.stopPropagation)
            event.stopPropagation();
        if (event.preventDefault)
            event.preventDefault();
        var isHorizontal = this.IsHorizontal;
        var elementOffsetSizeProp = isHorizontal ? "offsetWidth" : "offsetHeight";
        var elementOffsetProp = isHorizontal ? "offsetLeft" : "offsetTop";
        var mouseMovement = this.getMouseMovement(event, movingEle);
        var basis;
        if (this.IsPrevious)
            basis = this.Element[elementOffsetSizeProp] + mouseMovement;
        else
            basis = this.Element[elementOffsetSizeProp] - mouseMovement;
        this.Element.style['flex-basis'] = basis + "px";
        return basis;
    };
    FlexBasisResizeModel.prototype.getMouseMovement = function (event, movingEle) {
        var boundingBox = movingEle.nativeElement.getBoundingClientRect();
        if (this.IsHorizontal)
            return event.clientX - boundingBox.left;
        return event.clientY - boundingBox.top;
    };
    return FlexBasisResizeModel;
}());
export { FlexBasisResizeModel };
