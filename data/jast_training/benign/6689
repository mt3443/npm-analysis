var FlexGrowResizeModel = /** @class */ (function () {
    function FlexGrowResizeModel(FirstElements, SecondElements, IsHorizontal) {
        this.FirstElements = FirstElements;
        this.SecondElements = SecondElements;
        this.IsHorizontal = IsHorizontal;
    }
    FlexGrowResizeModel.prototype.resize = function (event, movingEle) {
        if (!this.FirstElements || !this.FirstElements[0])
            return;
        if (!this.SecondElements || !this.SecondElements[0])
            return;
        if (event.stopPropagation)
            event.stopPropagation();
        if (event.preventDefault)
            event.preventDefault();
        var firstEle = this.FirstElements[0];
        var secondEle = this.SecondElements[0];
        var curTotalFlexGrowAmount = parseFloat(firstEle.style['flex-grow']) + parseFloat(secondEle.style['flex-grow']);
        var isHorizontal = this.IsHorizontal;
        var eventMovementProp = isHorizontal ? "movementX" : "movementY";
        var elementOffsetSizeProp = isHorizontal ? "offsetWidth" : "offsetHeight";
        var elementOffsetProp = isHorizontal ? "offsetLeft" : "offsetTop";
        var gripperProp = isHorizontal ? "left" : "top";
        var totalSize = firstEle[elementOffsetSizeProp] + secondEle[elementOffsetSizeProp];
        var mouseMovement = this.getMouseMovement(event, movingEle); // event[eventMovementProp];
        var firstSize = firstEle[elementOffsetSizeProp] + mouseMovement;
        var secondSize = totalSize - firstSize;
        var gripperBorderSize = 5;
        for (var ele in this.FirstElements) {
            firstEle.style['flex-grow'] = Math.min(10000, Math.max(0.0, curTotalFlexGrowAmount * (firstSize / totalSize)));
        }
        for (var ele in this.SecondElements) {
            secondEle.style['flex-grow'] = Math.min(10000, Math.max(0.0, curTotalFlexGrowAmount * (secondSize / totalSize)));
        }
        return firstSize;
    };
    FlexGrowResizeModel.prototype.getMouseMovement = function (event, movingEle) {
        var boundingBox = movingEle.nativeElement.getBoundingClientRect();
        if (this.IsHorizontal)
            return event.clientX - boundingBox.left;
        return event.clientY - boundingBox.top;
    };
    return FlexGrowResizeModel;
}());
export { FlexGrowResizeModel };
