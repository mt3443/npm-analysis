(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('@angular/core'), require('rxjs/Subject'), require('exif-js'), require('pica/dist/pica')) :
	typeof define === 'function' && define.amd ? define(['exports', '@angular/core', 'rxjs/Subject', 'exif-js', 'pica/dist/pica'], factory) :
	(factory((global['ngx-pica'] = {}),global.ng.core,global.Rx,global.EXIF,global.pica));
}(this, (function (exports,core,Subject,EXIF,pica) { 'use strict';

pica = pica && pica.hasOwnProperty('default') ? pica['default'] : pica;

var NgxPicaErrorType;
(function (NgxPicaErrorType) {
    NgxPicaErrorType["NO_FILES_RECEIVED"] = "NO_FILES_RECEIVED";
    NgxPicaErrorType["CANVAS_CONTEXT_IDENTIFIER_NOT_SUPPORTED"] = "CANVAS_CONTEXT_IDENTIFIER_NOT_SUPPORTED";
    NgxPicaErrorType["NOT_BE_ABLE_TO_COMPRESS_ENOUGH"] = "NOT_BE_ABLE_TO_COMPRESS_ENOUGH";
})(NgxPicaErrorType || (NgxPicaErrorType = {}));

var NgxPicaExifService = (function () {
    function NgxPicaExifService() {
    }
    NgxPicaExifService.prototype.getExifOrientedImage = function (image) {
        return new Promise(function (resolve, reject) {
            EXIF.getData(image, function () {
                var allExifMetaData = EXIF.getAllTags(image), exifOrientation = allExifMetaData.Orientation;
                if (exifOrientation) {
                    var canvas = document.createElement('canvas'), ctx = canvas.getContext('2d'), width = image.width, height = image.height;
                    if ([5, 6, 7, 8].indexOf(exifOrientation) > -1) {
                        canvas.width = height;
                        canvas.height = width;
                    }
                    else {
                        canvas.width = width;
                        canvas.height = height;
                    }
                    if (ctx) {
                        // transform context before drawing image
                        switch (exifOrientation) {
                            case 2:
                                ctx.transform(-1, 0, 0, 1, width, 0);
                                break;
                            case 3:
                                ctx.transform(-1, 0, 0, -1, width, height);
                                break;
                            case 4:
                                ctx.transform(1, 0, 0, -1, 0, height);
                                break;
                            case 5:
                                ctx.transform(0, 1, 1, 0, 0, 0);
                                break;
                            case 6:
                                ctx.transform(0, 1, -1, 0, height, 0);
                                break;
                            case 7:
                                ctx.transform(0, -1, -1, 0, height, width);
                                break;
                            case 8:
                                ctx.transform(0, -1, 1, 0, 0, width);
                                break;
                            default:
                                ctx.transform(1, 0, 0, 1, 0, 0);
                        }
                        // Draw img into canvas
                        ctx.drawImage(image, 0, 0, width, height);
                        var img_1 = new Image();
                        img_1.width = width;
                        img_1.height = height;
                        img_1.onload = function () {
                            resolve(img_1);
                        };
                        img_1.src = canvas.toDataURL();
                    }
                }
                else {
                    resolve(image);
                }
            });
        });
    };
    NgxPicaExifService.decorators = [
        { type: core.Injectable },
    ];
    /** @nocollapse */
    NgxPicaExifService.ctorParameters = function () { return []; };
    return NgxPicaExifService;
}());

var NgxPicaService = (function () {
    function NgxPicaService(_ngxPicaExifService) {
        this._ngxPicaExifService = _ngxPicaExifService;
        this.picaResizer = new pica();
        this.MAX_STEPS = 20;
        if (!this.picaResizer || !this.picaResizer.resize) {
            this.picaResizer = new window.pica();
        }
    }
    /**
     * Resize images array
     * @param {File[]} files
     * @param {number} width
     * @param {number} height
     * @param {NgxPicaResizeOptionsInterface} options
     * @returns {Observable<File>}
     */
    /**
         * Resize images array
         * @param {File[]} files
         * @param {number} width
         * @param {number} height
         * @param {NgxPicaResizeOptionsInterface} options
         * @returns {Observable<File>}
         */
    NgxPicaService.prototype.resizeImages = /**
         * Resize images array
         * @param {File[]} files
         * @param {number} width
         * @param {number} height
         * @param {NgxPicaResizeOptionsInterface} options
         * @returns {Observable<File>}
         */
    function (files, width, height, options) {
        var _this = this;
        var resizedImage = new Subject.Subject();
        var totalFiles = files.length;
        if (totalFiles > 0) {
            var nextFile_1 = new Subject.Subject();
            var index_1 = 0;
            var subscription_1 = nextFile_1.subscribe(function (file) {
                _this.resizeImage(file, width, height, options).subscribe(function (imageResized) {
                    index_1++;
                    resizedImage.next(imageResized);
                    if (index_1 < totalFiles) {
                        nextFile_1.next(files[index_1]);
                    }
                    else {
                        resizedImage.complete();
                        subscription_1.unsubscribe();
                    }
                }, function (err) {
                    var ngxPicaError = {
                        file: file,
                        err: err
                    };
                    resizedImage.error(ngxPicaError);
                });
            });
            nextFile_1.next(files[index_1]);
        }
        else {
            var ngxPicaError = {
                err: NgxPicaErrorType.NO_FILES_RECEIVED
            };
            resizedImage.error(ngxPicaError);
            resizedImage.complete();
        }
        return resizedImage.asObservable();
    };
    /**
     * Resize image file
     *
     * @param {File} file
     * @param {number} width
     * @param {number} height
     * @param {NgxPicaResizeOptionsInterface} options
     * @returns {Observable<File>}
     */
    /**
         * Resize image file
         *
         * @param {File} file
         * @param {number} width
         * @param {number} height
         * @param {NgxPicaResizeOptionsInterface} options
         * @returns {Observable<File>}
         */
    NgxPicaService.prototype.resizeImage = /**
         * Resize image file
         *
         * @param {File} file
         * @param {number} width
         * @param {number} height
         * @param {NgxPicaResizeOptionsInterface} options
         * @returns {Observable<File>}
         */
    function (file, width, height, options) {
        var _this = this;
        var resizedImage = new Subject.Subject();
        var originCanvas = document.createElement('canvas');
        var ctx = originCanvas.getContext('2d');
        var img = new Image();
        if (ctx) {
            img.onload = function () {
                _this._ngxPicaExifService.getExifOrientedImage(img).then(function (orientedImage) {
                    window.URL.revokeObjectURL(img.src);
                    originCanvas.width = orientedImage.width;
                    originCanvas.height = orientedImage.height;
                    ctx.drawImage(orientedImage, 0, 0);
                    var imageData = ctx.getImageData(0, 0, orientedImage.width, orientedImage.height);
                    if (options && options.aspectRatio && options.aspectRatio.keepAspectRatio) {
                        var ratio = 0;
                        if (options.aspectRatio.forceMinDimensions) {
                            ratio = Math.max(width / imageData.width, height / imageData.height);
                        }
                        else {
                            ratio = Math.min(width / imageData.width, height / imageData.height);
                        }
                        width = Math.round(imageData.width * ratio);
                        height = Math.round(imageData.height * ratio);
                    }
                    var destinationCanvas = document.createElement('canvas');
                    destinationCanvas.width = width;
                    destinationCanvas.height = height;
                    _this.picaResize(file, originCanvas, destinationCanvas, options)
                        .catch(function (err) { return resizedImage.error(err); })
                        .then(function (imgResized) {
                        resizedImage.next(imgResized);
                    });
                });
            };
            img.src = window.URL.createObjectURL(file);
        }
        else {
            resizedImage.error(NgxPicaErrorType.CANVAS_CONTEXT_IDENTIFIER_NOT_SUPPORTED);
        }
        return resizedImage.asObservable();
    };
    /**
     * Compress images array
     *
     * @param {File[]} files
     * @param {number} sizeInMB
     * @returns {Observable<File>}
     */
    /**
         * Compress images array
         *
         * @param {File[]} files
         * @param {number} sizeInMB
         * @returns {Observable<File>}
         */
    NgxPicaService.prototype.compressImages = /**
         * Compress images array
         *
         * @param {File[]} files
         * @param {number} sizeInMB
         * @returns {Observable<File>}
         */
    function (files, sizeInMB) {
        var _this = this;
        var compressedImage = new Subject.Subject();
        var totalFiles = files.length;
        if (totalFiles > 0) {
            var nextFile_2 = new Subject.Subject();
            var index_2 = 0;
            var subscription_2 = nextFile_2.subscribe(function (file) {
                _this.compressImage(file, sizeInMB).subscribe(function (imageCompressed) {
                    index_2++;
                    compressedImage.next(imageCompressed);
                    if (index_2 < totalFiles) {
                        nextFile_2.next(files[index_2]);
                    }
                    else {
                        compressedImage.complete();
                        subscription_2.unsubscribe();
                    }
                }, function (err) {
                    var ngxPicaError = {
                        file: file,
                        err: err
                    };
                    compressedImage.error(ngxPicaError);
                });
            });
            nextFile_2.next(files[index_2]);
        }
        else {
            var ngxPicaError = {
                err: NgxPicaErrorType.NO_FILES_RECEIVED
            };
            compressedImage.error(ngxPicaError);
            compressedImage.complete();
        }
        return compressedImage.asObservable();
    };
    /**
     * Compress image file
     *
     * @param {File} file
     * @param {number} sizeInMB
     * @returns {Observable<File>}
     */
    /**
         * Compress image file
         *
         * @param {File} file
         * @param {number} sizeInMB
         * @returns {Observable<File>}
         */
    NgxPicaService.prototype.compressImage = /**
         * Compress image file
         *
         * @param {File} file
         * @param {number} sizeInMB
         * @returns {Observable<File>}
         */
    function (file, sizeInMB) {
        var _this = this;
        var compressedImage = new Subject.Subject();
        if (this.bytesToMB(file.size) <= sizeInMB) {
            setTimeout(function () {
                compressedImage.next(file);
            });
        }
        else {
            var originCanvas_1 = document.createElement('canvas');
            var ctx_1 = originCanvas_1.getContext('2d');
            var img_1 = new Image();
            if (ctx_1) {
                img_1.onload = function () {
                    _this._ngxPicaExifService.getExifOrientedImage(img_1).then(function (orientedImage) {
                        window.URL.revokeObjectURL(img_1.src);
                        originCanvas_1.width = orientedImage.width;
                        originCanvas_1.height = orientedImage.height;
                        ctx_1.drawImage(orientedImage, 0, 0);
                        _this.getCompressedImage(originCanvas_1, file.type, 1, sizeInMB, 0)
                            .catch(function (err) { return compressedImage.error(err); })
                            .then(function (blob) {
                            var imgCompressed = _this.blobToFile(blob, file.name, file.type, new Date().getTime());
                            compressedImage.next(imgCompressed);
                        });
                    });
                };
                img_1.src = window.URL.createObjectURL(file);
            }
            else {
                compressedImage.error(NgxPicaErrorType.CANVAS_CONTEXT_IDENTIFIER_NOT_SUPPORTED);
            }
        }
        return compressedImage.asObservable();
    };
    /**
     * Through Pica toBlob method, compress image file
     *
     * @param {HTMLCanvasElement} canvas
     * @param {string} type
     * @param {number} quality
     * @param {number} sizeInMB
     * @param {number} step
     * @returns {Promise<Blob>}
     */
    /**
         * Through Pica toBlob method, compress image file
         *
         * @param {HTMLCanvasElement} canvas
         * @param {string} type
         * @param {number} quality
         * @param {number} sizeInMB
         * @param {number} step
         * @returns {Promise<Blob>}
         */
    NgxPicaService.prototype.getCompressedImage = /**
         * Through Pica toBlob method, compress image file
         *
         * @param {HTMLCanvasElement} canvas
         * @param {string} type
         * @param {number} quality
         * @param {number} sizeInMB
         * @param {number} step
         * @returns {Promise<Blob>}
         */
    function (canvas, type, quality, sizeInMB, step) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            _this.picaResizer.toBlob(canvas, type, quality)
                .catch(function (err) { return reject(err); })
                .then(function (blob) {
                _this.checkCompressedImageSize(canvas, blob, quality, sizeInMB, step)
                    .catch(function (err) { return reject(err); })
                    .then(function (blob) {
                    resolve(blob);
                });
            });
        });
    };
    /**
     * Check if image has been compressed enough
     *
     * @param {HTMLCanvasElement} canvas
     * @param {Blob} blob
     * @param {number} quality
     * @param {number} sizeInMB
     * @param {number} step
     * @returns {Promise<Blob>}
     */
    /**
         * Check if image has been compressed enough
         *
         * @param {HTMLCanvasElement} canvas
         * @param {Blob} blob
         * @param {number} quality
         * @param {number} sizeInMB
         * @param {number} step
         * @returns {Promise<Blob>}
         */
    NgxPicaService.prototype.checkCompressedImageSize = /**
         * Check if image has been compressed enough
         *
         * @param {HTMLCanvasElement} canvas
         * @param {Blob} blob
         * @param {number} quality
         * @param {number} sizeInMB
         * @param {number} step
         * @returns {Promise<Blob>}
         */
    function (canvas, blob, quality, sizeInMB, step) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            if (step > _this.MAX_STEPS) {
                reject(NgxPicaErrorType.NOT_BE_ABLE_TO_COMPRESS_ENOUGH);
            }
            if (_this.bytesToMB(blob.size) < sizeInMB) {
                resolve(blob);
            }
            else {
                var newQuality = quality - (quality * 0.1);
                var newStep = step + 1;
                // recursively compression
                resolve(_this.getCompressedImage(canvas, blob.type, newQuality, sizeInMB, newStep));
            }
        });
    };
    /**
     * Through Pica resize method, resize image file
     *
     * @param {File} file
     * @param {HTMLCanvasElement} from
     * @param {HTMLCanvasElement} to
     * @param options
     * @returns {Promise<File>}
     */
    /**
         * Through Pica resize method, resize image file
         *
         * @param {File} file
         * @param {HTMLCanvasElement} from
         * @param {HTMLCanvasElement} to
         * @param options
         * @returns {Promise<File>}
         */
    NgxPicaService.prototype.picaResize = /**
         * Through Pica resize method, resize image file
         *
         * @param {File} file
         * @param {HTMLCanvasElement} from
         * @param {HTMLCanvasElement} to
         * @param options
         * @returns {Promise<File>}
         */
    function (file, from, to, options) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            _this.picaResizer.resize(from, to, options)
                .catch(function (err) { return reject(err); })
                .then(function (resizedCanvas) { return _this.picaResizer.toBlob(resizedCanvas, file.type); })
                .then(function (blob) {
                var fileResized = _this.blobToFile(blob, file.name, file.type, new Date().getTime());
                resolve(fileResized);
            });
        });
    };
    /**
     * Return new File from Blob
     *
     * @param {Blob} blob
     * @param {string} name
     * @param {string} type
     * @param {number} lastModified
     * @returns {File}
     */
    /**
         * Return new File from Blob
         *
         * @param {Blob} blob
         * @param {string} name
         * @param {string} type
         * @param {number} lastModified
         * @returns {File}
         */
    NgxPicaService.prototype.blobToFile = /**
         * Return new File from Blob
         *
         * @param {Blob} blob
         * @param {string} name
         * @param {string} type
         * @param {number} lastModified
         * @returns {File}
         */
    function (blob, name, type, lastModified) {
        return new File([blob], name, { type: type, lastModified: lastModified });
    };
    /**
     * Convert bytes to MegaBytes
     *
     * @param {number} bytes
     * @returns {number}
     */
    /**
         * Convert bytes to MegaBytes
         *
         * @param {number} bytes
         * @returns {number}
         */
    NgxPicaService.prototype.bytesToMB = /**
         * Convert bytes to MegaBytes
         *
         * @param {number} bytes
         * @returns {number}
         */
    function (bytes) {
        return bytes / 1048576;
    };
    NgxPicaService.decorators = [
        { type: core.Injectable },
    ];
    /** @nocollapse */
    NgxPicaService.ctorParameters = function () { return [
        { type: NgxPicaExifService, },
    ]; };
    return NgxPicaService;
}());

var NgxPicaImageService = (function () {
    function NgxPicaImageService() {
        this.imageExtensions = [
            "ase",
            "art",
            "bmp",
            "blp",
            "cd5",
            "cit",
            "cpt",
            "cr2",
            "cut",
            "dds",
            "dib",
            "djvu",
            "egt",
            "exif",
            "gif",
            "gpl",
            "grf",
            "icns",
            "ico",
            "iff",
            "jng",
            "jpeg",
            "jpg",
            "jfif",
            "jp2",
            "jps",
            "lbm",
            "max",
            "miff",
            "mng",
            "msp",
            "nitf",
            "ota",
            "pbm",
            "pc1",
            "pc2",
            "pc3",
            "pcf",
            "pcx",
            "pdn",
            "pgm",
            "PI1",
            "PI2",
            "PI3",
            "pict",
            "pct",
            "pnm",
            "pns",
            "ppm",
            "psb",
            "psd",
            "pdd",
            "psp",
            "px",
            "pxm",
            "pxr",
            "qfx",
            "raw",
            "rle",
            "sct",
            "sgi",
            "rgb",
            "int",
            "bw",
            "tga",
            "tiff",
            "tif",
            "vtf",
            "xbm",
            "xcf",
            "xpm",
            "3dv",
            "amf",
            "ai",
            "awg",
            "cgm",
            "cdr",
            "cmx",
            "dxf",
            "e2d",
            "egt",
            "eps",
            "fs",
            "gbr",
            "odg",
            "svg",
            "stl",
            "vrml",
            "x3d",
            "sxd",
            "v2d",
            "vnd",
            "wmf",
            "emf",
            "art",
            "xar",
            "png",
            "webp",
            "jxr",
            "hdp",
            "wdp",
            "cur",
            "ecw",
            "iff",
            "lbm",
            "liff",
            "nrrd",
            "pam",
            "pcx",
            "pgf",
            "sgi",
            "rgb",
            "rgba",
            "bw",
            "int",
            "inta",
            "sid",
            "ras",
            "sun",
            "tga"
        ];
    }
    /**
     * Check if given file is an image or not
     *
     * @param {File} file
     * @returns {boolean}
     */
    /**
         * Check if given file is an image or not
         *
         * @param {File} file
         * @returns {boolean}
         */
    NgxPicaImageService.prototype.isImage = /**
         * Check if given file is an image or not
         *
         * @param {File} file
         * @returns {boolean}
         */
    function (file) {
        var fileExtension = file.name.toLowerCase().substr(file.name.lastIndexOf('.') + 1);
        return (this.imageExtensions.indexOf(fileExtension) !== -1);
    };
    NgxPicaImageService.decorators = [
        { type: core.Injectable },
    ];
    /** @nocollapse */
    NgxPicaImageService.ctorParameters = function () { return []; };
    return NgxPicaImageService;
}());

var NgxPicaModule = (function () {
    function NgxPicaModule() {
    }
    NgxPicaModule.decorators = [
        { type: core.NgModule, args: [{
                    providers: [
                        { provide: NgxPicaService, useClass: NgxPicaService },
                        { provide: NgxPicaExifService, useClass: NgxPicaExifService },
                        { provide: NgxPicaImageService, useClass: NgxPicaImageService },
                    ]
                },] },
    ];
    /** @nocollapse */
    NgxPicaModule.ctorParameters = function () { return []; };
    return NgxPicaModule;
}());

exports.NgxPicaModule = NgxPicaModule;
exports.NgxPicaService = NgxPicaService;
exports.NgxPicaImageService = NgxPicaImageService;

Object.defineProperty(exports, '__esModule', { value: true });

})));
