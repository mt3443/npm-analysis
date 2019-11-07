var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, ChangeDetectionStrategy, Component, Input, ViewChild, ViewContainerRef } from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { JitComponent } from '../../../controls/components/base/components/jit-component';
var FormTemplateComponent = /** @class */ (function () {
    function FormTemplateComponent(
        //private viewContainer: ViewContainerRef,
        changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        changeDetectorRef.detach();
    }
    FormTemplateComponent.prototype.ngOnInit = function () {
        if (this.Property.IsTemplate) {
            var type = this.Property;
            if (!type.TemplateComponent) {
                type.TemplateComponent = JitComponent.createComponent(type.Template, type.TemplateModules);
            }
            var container = this.viewContainer.createComponent(type.TemplateComponent);
            container.instance.Property = this.Property;
            container.changeDetectorRef.detectChanges();
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", Property)
    ], FormTemplateComponent.prototype, "Property", void 0);
    __decorate([
        ViewChild('container', { read: ViewContainerRef }),
        __metadata("design:type", ViewContainerRef)
    ], FormTemplateComponent.prototype, "viewContainer", void 0);
    FormTemplateComponent = __decorate([
        Component({
            selector: 'pm-form-template',
            template: '<ng-template #container></ng-template>',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], FormTemplateComponent);
    return FormTemplateComponent;
}());
export { FormTemplateComponent };
