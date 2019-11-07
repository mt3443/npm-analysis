var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ApplicationRef, ComponentFactoryResolver, Injectable, Injector } from '@angular/core';
import { ModalDialog } from '../../../controls/components/modal/modal-dialog';
var DialogService = /** @class */ (function () {
    function DialogService(applicationRef, componentFactoryResolver, injector) {
        this.applicationRef = applicationRef;
        this.componentFactoryResolver = componentFactoryResolver;
        this.injector = injector;
    }
    DialogService.prototype.getRootViewContainer = function () {
        if (this.container)
            return this.container;
        var rootComponents = this.applicationRef['components'];
        if (rootComponents.length)
            return rootComponents[0];
        return undefined;
        //throw new Error('View Container not found! ngUpgrade needs to manually set this via setRootViewContainer.');
    };
    DialogService.prototype.setRootViewContainer = function (container) {
        this.container = container;
    };
    DialogService.prototype.getComponentRootNode = function (componentRef) {
        return componentRef.hostView.rootNodes[0];
    };
    DialogService.prototype.getRootViewContainerNode = function () {
        var container = this.getRootViewContainer();
        if (container)
            return this.getComponentRootNode(container);
        return undefined;
    };
    DialogService.prototype.projectComponentInputs = function (component, options) {
        if (options) {
            var props = Object.getOwnPropertyNames(options);
            for (var _i = 0, props_1 = props; _i < props_1.length; _i++) {
                var prop = props_1[_i];
                component.instance[prop] = options[prop];
            }
        }
        return component;
    };
    DialogService.prototype.ShowInstance = function (
        //componentClass: Type<any>,
        instance, options, location) {
        if (options === void 0) { options = {}; }
        if (location === void 0) { location = this.getRootViewContainerNode(); }
        // it is possible that the app is not fully initialized yet.
        if (!location)
            return undefined;
        var component = instance.constructor;
        var componentFactory = this.componentFactoryResolver.resolveComponentFactory(component);
        //let componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentClass);
        var componentRef = componentFactory.create(this.injector);
        var appRef = this.applicationRef;
        var componentRootNode = this.getComponentRootNode(componentRef);
        // project the options passed to the component instance
        this.projectComponentInputs(componentRef, options);
        if (appRef['attachView']) {
            appRef.attachView(componentRef.hostView);
            componentRef.onDestroy(function () {
                appRef.detachView(componentRef.hostView);
            });
        }
        location.appendChild(componentRootNode);
        if (componentRef.instance instanceof ModalDialog) {
            var dialog = componentRef.instance;
            if (dialog) {
                dialog.OnClosed.subscribe(function (val) {
                    componentRef.destroy();
                });
            }
        }
        return componentRef;
    };
    DialogService.prototype.Show = function (componentClass, options, location) {
        if (options === void 0) { options = {}; }
        if (location === void 0) { location = this.getRootViewContainerNode(); }
        // it is possible that the app is not fully initialized yet.
        if (!location)
            return undefined;
        var componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentClass);
        var componentRef = componentFactory.create(this.injector);
        var appRef = this.applicationRef;
        var componentRootNode = this.getComponentRootNode(componentRef);
        // project the options passed to the component instance
        this.projectComponentInputs(componentRef, options);
        if (appRef['attachView']) {
            appRef.attachView(componentRef.hostView);
            componentRef.onDestroy(function () {
                appRef.detachView(componentRef.hostView);
            });
        }
        location.appendChild(componentRootNode);
        if (componentRef.instance instanceof ModalDialog) {
            var dialog = componentRef.instance;
            if (dialog) {
                dialog.Initialize();
                dialog.OnClosed.subscribe(function (val) {
                    dialog.Destroy();
                    componentRef.destroy();
                });
            }
        }
        return componentRef.instance;
    };
    DialogService = __decorate([
        Injectable(),
        __metadata("design:paramtypes", [ApplicationRef,
            ComponentFactoryResolver,
            Injector])
    ], DialogService);
    return DialogService;
}());
export { DialogService };
