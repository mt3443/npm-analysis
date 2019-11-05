import { Component, Directive, ElementRef, Injectable, NgModule, Pipe, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateService } from '@ngx-translate/core';
import { MatIconModule, MatInputModule, MatSidenavModule } from '@angular/material';
import { TreeModule } from 'angular-tree-component';

var MxNestedMenuComponent = (function () {
    /**
     * @param {?} translate
     */
    function MxNestedMenuComponent(translate) {
        this.translate = translate;
        this.nodes = [
            {
                id: 1,
                name: 'System',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 1.1,
                        name: 'System Management',
                        href: '#',
                        children: [
                            { id: 1.11, name: 'Information Setting', href: '#' },
                            { id: 1.12, name: 'Firmware Upgrade', href: '#' },
                            { id: 1.13, name: 'Configuration Backup and Restore', href: '#' },
                            { id: 1.14, name: 'Event Log Backup', href: '#' },
                            { id: 1.15, name: 'DIP', href: '#' }
                        ]
                    },
                    {
                        id: 1.2,
                        name: 'Account Management',
                        href: '#',
                        children: [
                            { id: 1.21, name: 'User Account', href: '#' },
                            { id: 1.22, name: 'Password Policy', href: '#' }
                        ]
                    },
                    {
                        id: 1.3,
                        name: 'Network',
                        href: '#',
                        children: [
                            { id: 1.31, name: 'IP Configuration', href: '#' },
                            { id: 1.32, name: 'DHCP Server', href: '#' },
                            { id: 1.33, name: 'DHCP Relay', href: '#' }
                        ]
                    },
                    {
                        id: 1.4,
                        name: 'Time',
                        href: '#',
                        children: [
                            { id: 1.41, name: 'Time Zone ', href: '#' },
                            { id: 1.42, name: 'System Time', href: '#' },
                            { id: 1.43, name: 'IEEE1588 PTP', href: '#' }
                        ]
                    }
                ]
            },
            {
                id: 2,
                name: 'Port',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 2.1,
                        name: 'Port Interface',
                        href: '#',
                        children: [
                            { id: 2.11, name: 'Port Configuration', href: '#' },
                            { id: 2.12, name: 'Jumbo Frame', href: '#' },
                            { id: 2.13, name: 'Link Delay', href: '#' }
                        ]
                    },
                    {
                        id: 2.2,
                        name: 'Link Aggregation',
                        href: '#',
                        children: [
                            { id: 2.21, name: 'Static Trunk / LACP', href: '#' },
                        ]
                    },
                    {
                        id: 2.3,
                        name: 'PoE',
                        href: '#',
                        children: [
                            { id: 2.31, name: 'PoE Setting', href: '#' },
                        ]
                    }
                ]
            },
            {
                id: 3,
                name: 'Layer 2 Switching',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 3.1,
                        name: 'VLAN',
                        href: '#',
                        children: [
                            { id: 3.11, name: 'VLAN Mode / Port Role', href: '#' },
                            { id: 3.12, name: 'IEEE802.1Q VLAN', href: '#' },
                            { id: 3.13, name: 'QinQ', href: '#' }
                        ]
                    },
                    {
                        id: 3.2,
                        name: 'MAC',
                        href: '#',
                        children: [
                            { id: 3.21, name: 'Timer Setting', href: '#' },
                            { id: 3.22, name: 'MAC Entry', href: '#' },
                        ]
                    },
                    {
                        id: 3.3,
                        name: 'QoS',
                        href: '#',
                        children: [
                            { id: 3.31, name: 'Classification', href: '#' },
                            { id: 3.32, name: 'Ingress Rate Limit', href: '#' },
                            { id: 3.33, name: 'Scheduler', href: '#' },
                            { id: 3.34, name: 'Egress Shaper', href: '#' }
                        ]
                    },
                    {
                        id: 3.4,
                        name: 'Multicast',
                        href: '#',
                        children: [
                            { id: 3.41, name: 'IGMP Snooping', href: '#' },
                            { id: 3.42, name: 'GMRP', href: '#' },
                            { id: 3.43, name: 'Static Multicast', href: '#' },
                            { id: 3.44, name: 'Multicast Table', href: '#' }
                        ]
                    },
                    {
                        id: 3.5,
                        name: 'GARP/MRP',
                        href: '#',
                        children: [
                            { id: 3.51, name: 'GARP', href: '#' },
                            { id: 3.52, name: 'MRP', href: '#' }
                        ]
                    }
                ]
            },
            {
                id: 4,
                name: 'Layer 3 Routing',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 4.1,
                        name: 'IP Interface',
                        href: '#',
                        children: [
                            { id: 4.11, name: 'IP Interface Configuration', href: '#' }
                        ]
                    },
                    {
                        id: 4.2,
                        name: 'Unicast Route',
                        href: '#',
                        children: [
                            { id: 4.21, name: 'Static Route', href: '#' },
                            { id: 4.22, name: 'RIP', href: '#' },
                            { id: 4.23, name: 'OSPF', href: '#' },
                            { id: 4.24, name: 'Routing Table', href: '#' }
                        ]
                    },
                    {
                        id: 4.3,
                        name: 'Multicast Route',
                        href: '#',
                        children: [
                            { id: 4.31, name: 'Multicast Local Route', href: '#' },
                            { id: 4.32, name: 'DVMRP', href: '#' },
                            { id: 4.33, name: 'PIM', href: '#' }
                        ]
                    }
                ]
            },
            {
                id: 5,
                name: 'Network Redundancy',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 5.1,
                        name: 'Layer 2 Redundancy',
                        href: '#',
                        children: [
                            { id: 5.11, name: 'Spanning Tree', href: '#' },
                            { id: 5.12, name: 'Turbo Ring V2', href: '#' },
                            { id: 5.13, name: 'Turbo Chain', href: '#' },
                            { id: 5.14, name: 'Dual Homing', href: '#' },
                            { id: 5.15, name: 'Multiple Coupling ', href: '#' },
                            { id: 5.16, name: 'MRP', href: '#' },
                            { id: 5.17, name: 'PRP', href: '#' },
                            { id: 5.18, name: 'HSR', href: '#' },
                            { id: 5.19, name: 'RSTP grouping', href: '#' },
                        ]
                    },
                    {
                        id: 5.2,
                        name: 'Layer 3 Redundancy',
                        href: '#',
                        children: [
                            { id: 5.21, name: 'VRRP', href: '#' }
                        ]
                    }
                ]
            },
            {
                id: 6,
                name: 'Network Redundancy',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 6.1,
                        name: 'Network Management',
                        href: '#',
                        children: [
                            { id: 6.11, name: 'SNMP', href: '#' },
                            { id: 6.12, name: 'SNMP Trap/Inform', href: '#' },
                        ]
                    },
                    {
                        id: 6.2,
                        name: 'Industrial Protocol',
                        href: '#',
                        children: [
                            { id: 6.21, name: 'EtherNet/IP', href: '#' },
                            { id: 6.22, name: 'Modbus/TCP', href: '#' },
                            { id: 6.23, name: 'PROFINET', href: '#' },
                        ]
                    }
                ]
            },
            {
                id: 7,
                name: 'Security',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 7.1,
                        name: 'Device Securityt',
                        href: '#',
                        children: [
                            { id: 7.11, name: 'Management Interface', href: '#' },
                            { id: 7.12, name: 'Login Policy', href: '#' },
                            { id: 7.12, name: 'Trusted Access', href: '#' },
                            { id: 7.12, name: 'SSL Certificate Management', href: '#' },
                            { id: 7.12, name: 'SSH Key Management', href: '#' },
                        ]
                    },
                    {
                        id: 7.2,
                        name: 'Network Security',
                        href: '#',
                        children: [
                            { id: 7.21, name: 'IEEE802.1X', href: '#' },
                            { id: 7.22, name: 'Port Security', href: '#' },
                            { id: 7.23, name: 'MAC Authentication Bypass', href: '#' },
                            { id: 7.24, name: 'Access Control List', href: '#' },
                            { id: 7.25, name: 'Storm Control', href: '#' },
                            { id: 7.26, name: 'Loop Protection', href: '#' },
                        ]
                    },
                    {
                        id: 7.3,
                        name: 'Authentication',
                        href: '#',
                        children: [
                            { id: 7.31, name: 'Authentication Mode', href: '#' },
                            { id: 7.32, name: 'RADIUS', href: '#' },
                            { id: 7.33, name: 'TACACS+', href: '#' },
                        ]
                    }
                ]
            },
            {
                id: 8,
                name: 'Diagnostics',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 8.1,
                        name: 'System Status',
                        href: '#',
                        children: [
                            { id: 8.11, name: 'Utilization', href: '#' },
                            { id: 8.12, name: 'Statistics', href: '#' }
                        ]
                    },
                    {
                        id: 8.2,
                        name: 'Event Notification',
                        href: '#',
                        children: [
                            { id: 8.21, name: 'Event Setting', href: '#' },
                            { id: 8.22, name: 'Email Notification', href: '#' },
                            { id: 8.23, name: 'Syslog', href: '#' },
                            { id: 8.24, name: 'Event Log', href: '#' },
                        ]
                    },
                    {
                        id: 8.3,
                        name: 'Diagnosis',
                        href: '#',
                        children: [
                            { id: 8.31, name: 'LLDP', href: '#' },
                            { id: 8.32, name: 'Traffic Mirror', href: '#' },
                            { id: 8.33, name: 'Fiber Check', href: '#' },
                            { id: 8.34, name: 'PoE Configuration Helper', href: '#' },
                            { id: 8.35, name: 'PD Health Check', href: '#' },
                            { id: 8.36, name: 'Ping', href: '#' },
                            { id: 8.37, name: 'Traceroute', href: '#' },
                            { id: 8.38, name: 'ARP Table', href: '#' },
                        ]
                    }
                ]
            },
            {
                id: 9,
                name: 'Application',
                href: '#',
                icon: '',
                children: [
                    {
                        id: 9.1,
                        name: 'Substation Automation',
                        href: '#',
                        children: [
                            { id: 9.11, name: 'IEC 61850 QoS', href: '#' },
                            { id: 9.12, name: 'GOOSE Check', href: '#' },
                            { id: 9.13, name: 'MMS', href: '#' },
                            { id: 9.14, name: 'R-GOOSE', href: '#' },
                            { id: 9.15, name: 'SMV Check', href: '#' },
                        ]
                    }
                ]
            },
        ];
        /*   nodes = [
            {
              id: 1,
              name: 'root1',
              children: [
                { id: 2, name: 'child1' },
                { id: 3, name: 'child2' }
              ]
            },
            {
              id: 4,
              name: 'root2',
              children: [
                { id: 5, name: 'child2.1' },
                {
                  id: 6,
                  name: 'child2.2',
                  children: [
                    { id: 7, name: 'subsub' }
                  ]
                }
              ]
            },
            {
              id: 8,
              name: 'root3',
              children: [
                { id: 9, name: 'child1' },
                { id: 10, name: 'child2' }
              ]
            },
            {
              id: 11,
              name: 'root4',
              children: [
                { id: 12, name: 'child4.1' },
                {
                  id: 13,
                  name: 'child4.2',
                  children: [
                    { id: 14, name: 'child4.2.1' },
                    {
                      id: 15,
                      name: 'child4.2.2',
                      children: [
                        { id: 16, name: 'child4.2.2.1' },
                        {
                          id: 17,
                          name: 'child4.2.2.1',
                          children: [
                            { id: 18, name: 'subsub' }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]; */
        this.options = {
            displayField: 'name',
            isExpandedField: 'expanded',
            levelPadding: '10px',
            idField: 'id',
            allowDrag: function (node) {
                return false;
            },
            allowDrop: function (node) {
                return false;
            },
            useVirtualScroll: true,
            animateExpand: true,
            animateSpeed: 30,
            animateAcceleration: 1.2,
            treeNodeTemplate: "\n    <mat-icon>search</mat-icon>\n    <a *ngIf=\"node.data.href\" href=\"node.data.href\">{{ node.data.name }}</a>\n    <span *ngIf=\"!node.data.href\">{{ node.data.name }}</span>\n    "
        };
        this.sidenav.open();
    }
    /**
     * @return {?}
     */
    MxNestedMenuComponent.prototype.toggleMenu = function () {
        this.sidenav.toggle();
    };
    /**
     * @return {?}
     */
    MxNestedMenuComponent.prototype.filterNodes = function () {
        console.log('input text  -----> ' + this.jumppage.nativeElement.value);
        if (this.jumppage.nativeElement.value === '') {
            this.tree.treeModel.clearFilter();
            if (this.tree.treeModel.getActiveNode()) {
                this.tree.treeModel.setFocus(this.tree.treeModel.getActiveNode());
            }
            else {
                this.tree.treeModel.collapseAll();
            }
        }
        else {
            this.tree.treeModel.filterNodes(this.jumppage.nativeElement.value, true);
        }
    };
    
    return MxNestedMenuComponent;
}());
MxNestedMenuComponent.decorators = [
    { type: Component, args: [{
                selector: 'mx-nested-menu-component',
                template: "<mat-sidenav #sidenav mode=\"side\" class=\"app-sidenav\" fxLayout=\"column\" name=\"sidenav\"> <div class=\"jump-block\"> <mat-input-container> <!-- <input matInput placeholder=\"{{ 'general.menu.jump_page_placeholder' | translate }}\" name=\"jumppage\"> --> <input matInput #jumppage placeholder=\"Type keyword to search111\" name=\"jumppage\" (keyup)=\"filterNodes()\"> <mat-icon (click)=\"filterNodes()\">search</mat-icon> </mat-input-container> </div> <div class=\"menu-block\"> <tree-root #tree [nodes]=\"nodes\" [focused]=\"true\" [options]=\"options\"></tree-root> </div> </mat-sidenav>",
                styles: [""]
            },] },
];
/**
 * @nocollapse
 */
MxNestedMenuComponent.ctorParameters = function () { return [
    { type: TranslateService, },
]; };
MxNestedMenuComponent.propDecorators = {
    'tree': [{ type: ViewChild, args: ['tree',] },],
    'sidenav': [{ type: ViewChild, args: ['sidenav',] },],
    'jumppage': [{ type: ViewChild, args: ['jumppage',] },],
};

var MxNestedMenuDirective = (function () {
    /**
     * @param {?} el
     */
    function MxNestedMenuDirective(el) {
        this.el = el;
    }
    return MxNestedMenuDirective;
}());
MxNestedMenuDirective.decorators = [
    { type: Directive, args: [{
                selector: '[mxNestedMenuDirective]'
            },] },
];
/**
 * @nocollapse
 */
MxNestedMenuDirective.ctorParameters = function () { return [
    { type: ElementRef, },
]; };

/**
 * Transforms any input value
 */
var MxNestedMenuPipe = (function () {
    function MxNestedMenuPipe() {
    }
    /**
     * @param {?} value
     * @param {?=} args
     * @return {?}
     */
    MxNestedMenuPipe.prototype.transform = function (value, args) {
        if (args === void 0) { args = null; }
        return value;
    };
    return MxNestedMenuPipe;
}());
MxNestedMenuPipe.decorators = [
    { type: Pipe, args: [{
                name: 'mxNestedMenuPipe'
            },] },
    { type: Injectable },
];
/**
 * @nocollapse
 */
MxNestedMenuPipe.ctorParameters = function () { return []; };

var MxNestedMenuService = (function () {
    function MxNestedMenuService() {
    }
    return MxNestedMenuService;
}());
MxNestedMenuService.decorators = [
    { type: Injectable },
];
/**
 * @nocollapse
 */
MxNestedMenuService.ctorParameters = function () { return []; };

var MxNestedMenuModule = (function () {
    function MxNestedMenuModule() {
    }
    /**
     * @return {?}
     */
    MxNestedMenuModule.forRoot = function () {
        return {
            ngModule: MxNestedMenuModule,
            providers: [MxNestedMenuService]
        };
    };
    return MxNestedMenuModule;
}());
MxNestedMenuModule.decorators = [
    { type: NgModule, args: [{
                imports: [
                    CommonModule,
                    MatIconModule,
                    MatInputModule,
                    MatSidenavModule,
                    TreeModule,
                ],
                declarations: [
                    MxNestedMenuComponent,
                    MxNestedMenuDirective,
                    MxNestedMenuPipe
                ],
                exports: [
                    MxNestedMenuComponent,
                    MxNestedMenuDirective,
                    MxNestedMenuPipe
                ]
            },] },
];
/**
 * @nocollapse
 */
MxNestedMenuModule.ctorParameters = function () { return []; };

export { MxNestedMenuModule, MxNestedMenuComponent, MxNestedMenuDirective, MxNestedMenuPipe, MxNestedMenuService };
