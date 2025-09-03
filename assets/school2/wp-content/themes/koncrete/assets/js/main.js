"use strict";

(function($) {


    var calculateWpAdminHeight = function() {
        var wpadminbar = $('#wpadminbar');
        var wpadminbarHeight = 0;
        if (wpadminbar) {
            wpadminbarHeight = wpadminbar.outerHeight();
        }
        return wpadminbarHeight;
    }
    var calculateMeanMenuHeight = function() {
        var meanMenu = $('.mean-bar');
        var meanHeight = 0;
        if (meanMenu) {
            meanHeight = meanMenu.outerHeight();
        }
        return meanHeight ? meanHeight : 0;
    }
    var calculateMenuHeight = function() {
        var headerMenu = $('.header-menu-area');
        var menuHeight = 0;
        if (headerMenu) {
            menuHeight = headerMenu.outerHeight();
        }
        return menuHeight ? menuHeight : 0;
    }

    var calculateExtraOffset = function() {
        var extraOffset = 0;
        if ($('body').hasClass('has-sticky-menu')) {
            var meanMenuHeight = calculateMeanMenuHeight();
            var menuHeight = calculateMenuHeight();
            extraOffset = meanMenuHeight ? meanMenuHeight : menuHeight;
        }
        return extraOffset;
    }

    function rdtheme_wc_scripts($) {
        /* Shop change view */
        $('#shop-view-mode li a').on('click', function() {
            $('body').removeClass('product-grid-view product-list-view');

            if ($(this).closest('li').hasClass('list-view-nav')) {
                $('body').addClass('product-list-view');
                Cookies.set('shopview', 'list');
            } else {
                $('body').addClass('product-grid-view');
                Cookies.remove('shopview');
            }
            return false;
        });
    }
    // Wishlist Icon
    $(document).on('click', '.rdtheme-wishlist-icon', function() {
        if ($(this).hasClass('rdtheme-add-to-wishlist')) {

            var $obj = $(this),
                productId = $obj.data('product-id'),
                afterTitle = $obj.data('title-after');

            var data = {
                'action': 'koncrete_add_to_wishlist',
                'context': 'frontend',
                'nonce': $obj.data('nonce'),
                'add_to_wishlist': productId,
            };

            $.ajax({
                url: localizedObj.ajaxurl,
                type: 'POST',
                data: data,
                success: function(data) {
                    if (data['result'] != 'error') {
                        $obj.find('.wishlist-icon').removeClass('fa-heart-o').addClass('fa-heart').show();
                        $obj.removeClass('rdtheme-add-to-wishlist').addClass('rdtheme-remove-from-wishlist');
                        $obj.attr('title', afterTitle);
                    }
                }
            });

            return false;
        }
    });



    /*-------------------------------------
    ## Section background image
    -------------------------------------*/
    function imageFunction() {
        $('[data-bg-image]').each(function() {
            var img = $(this).data('bg-image');
            $(this).css({
                backgroundImage: 'url(' + img + ')',
            });
        });
    }


    function onReadyScripts() {
        /*-------------------------------------
        ## isotope initialization
        -------------------------------------*/
        $('.isotope-wrap').each(function() {
            var $container = $(this);
            var $isotope = $container.find('.featuredContainer').imagesLoaded(function() {
                $isotope.isotope({
                    filter: '*',
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false
                    }
                });
            });
            $container.find('.isotope-classes-tab').on('click', 'a', function() {
                var $this = $(this);
                $this.parent('.isotope-classes-tab').find('a').removeClass('current');
                $this.addClass('current');
                var selector = $this.attr('data-filter');
                $isotope.isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false
                    }
                });
                return false;
            });
        });

        /*-------------------------------------
        ## Carousel slider initiation
        -------------------------------------*/
        if ($.fn.owlCarousel) {

            function createCarousel(carousel) {

                var loop = carousel.data('loop'),
                    items = carousel.data('items'),
                    margin = carousel.data('margin'),
                    stagePadding = carousel.data('stage-padding'),
                    autoplay = carousel.data('autoplay'),
                    autoplayTimeout = carousel.data('autoplay-timeout'),
                    smartSpeed = carousel.data('smart-speed'),
                    dots = carousel.data('dots'),
                    nav = carousel.data('nav'),
                    navSpeed = carousel.data('nav-speed'),
                    rXsmall = carousel.data('r-x-small'),
                    rXsmallNav = carousel.data('r-x-small-nav'),
                    rXsmallDots = carousel.data('r-x-small-dots'),
                    rXmedium = carousel.data('r-x-medium'),
                    rXmediumNav = carousel.data('r-x-medium-nav'),
                    rXmediumDots = carousel.data('r-x-medium-dots'),
                    rSmall = carousel.data('r-small'),
                    rSmallNav = carousel.data('r-small-nav'),
                    rSmallDots = carousel.data('r-small-dots'),
                    rMedium = carousel.data('r-medium'),
                    rMediumNav = carousel.data('r-medium-nav'),
                    rMediumDots = carousel.data('r-medium-dots'),
                    rLarge = carousel.data('r-large'),
                    rLargeNav = carousel.data('r-large-nav'),
                    rLargeDots = carousel.data('r-large-dots'),
                    rExtraLarge = carousel.data('r-extra-large'),
                    rExtraLargeNav = carousel.data('r-extra-large-nav'),
                    rExtraLargeDots = carousel.data('r-extra-large-dots'),
                    center = carousel.data('center'),
                    custom_nav = carousel.data('custom-nav') || '';
                carousel.addClass('owl-carousel');
                var owl = carousel.owlCarousel({
                    loop: (loop ? true : false),
                    items: (items ? items : 4),
                    lazyLoad: true,
                    margin: (margin ? margin : 0),
                    autoplay: (autoplay ? true : false),
                    autoplayTimeout: (autoplayTimeout ? autoplayTimeout : 1000),
                    smartSpeed: (smartSpeed ? smartSpeed : 250),
                    dots: (dots ? true : false),
                    nav: (nav ? true : false),
                    navText: ['<i class="fas fa-chevron-left"></i>', '<i class="fas fa-chevron-right"></i>'],
                    navSpeed: (navSpeed ? true : false),
                    center: (center ? true : false),
                    responsiveClass: true,
                    responsive: {
                        0: {
                            items: (rXsmall ? rXsmall : 1),
                            nav: (rXsmallNav ? true : false),
                            dots: (rXsmallDots ? true : false)
                        },
                        576: {
                            items: (rXmedium ? rXmedium : 2),
                            nav: (rXmediumNav ? true : false),
                            dots: (rXmediumDots ? true : false)
                        },
                        768: {
                            items: (rSmall ? rSmall : 3),
                            nav: (rSmallNav ? true : false),
                            dots: (rSmallDots ? true : false)
                        },
                        992: {
                            items: (rMedium ? rMedium : 4),
                            nav: (rMediumNav ? true : false),
                            dots: (rMediumDots ? true : false)
                        },
                        1200: {
                            items: (rLarge ? rLarge : 5),
                            nav: (rLargeNav ? true : false),
                            dots: (rLargeDots ? true : false)
                        },
                        1400: {
                            items: (rExtraLarge ? rExtraLarge : 6),
                            nav: (rExtraLargeNav ? true : false),
                            dots: (rExtraLargeDots ? true : false)
                        }
                    }
                });
                if (custom_nav) {
                    var nav = $(custom_nav),
                        nav_next = $('.rt-next', nav),
                        nav_prev = $('.rt-prev', nav);

                    nav_next.on('click', function(e) {
                        e.preventDefault();
                        owl.trigger('next.owl.carousel');
                        return false;
                    });

                    nav_prev.on('click', function(e) {
                        e.preventDefault();
                        owl.trigger('prev.owl.carousel');
                        return false;
                    });
                }

            }

            $('.rc-carousel').each(function() {
                var carousel = $(this),
                    options = $.extend({
                        trigger_start: '',
                        trigger_end: '',
                    }, carousel.data('options'));


                if (!options.trigger_start && !options.trigger_end) {
                    createCarousel(carousel);

                } else {
                    var tempOwl = '';
                    $(window).on('resize load', function() {
                        var wW = $(window).width();

                        if (wW <= options.trigger_start) {
                            createCarousel(carousel);
                            console.log('called', 'create')
                        } else {
                            carousel.owlCarousel('destroy').removeClass('owl-carousel');
                        }

                    });
                }
            });
        }

        /*-------------------------------------
        ## Accordion
        -------------------------------------*/
        var accordion = $('#accordion');
        accordion.on('show.bs.collapse', function(e) {
            $(e.target).prev('.panel-heading').addClass('active');
        }).on('hide.bs.collapse', function(e) {
            $(e.target).prev('.panel-heading').removeClass('active');
        });

        $('.panel-heading a', accordion).on('click', function(e) {
            if ($(this).parents('.panel').children('.panel-collapse').hasClass('show')) {
                e.preventDefault();
                e.stopPropagation();
            }
        });




        //
        /*-------------------------------------
        ## for accordion widget
        -------------------------------------*/

        $('.rt-accordion').each(function() {
            var id = $(this).data('id');
            accordion = $('#' + id);
            accordion.on('show.bs.collapse', function(e) {
                $(e.target).prev('.panel-heading').addClass('active');
            }).on('hide.bs.collapse', function(e) {
                $(e.target).prev('.panel-heading').removeClass('active');
            });
        })



        /*-------------------------------------
        ## for making image background
        -------------------------------------*/
        imageFunction();



        /*-------------------------------------
        ## On Scroll function call if body
        ## has has-sticky-menu class
        -------------------------------------*/
        function stickInParent() {
            var offsetTop = calculateWpAdminHeight();
            $(".header-menu-area").stick_in_parent({
                parent: 'body',
                sticky_class: 'is-menu-stuck',
                offset_top: offsetTop,
            });
        }

        if ($('body').hasClass('has-sticky-menu')) {
            stickInParent();
        }

        /***************************************
        ## jquery Scollup activation code
        ***************************************/
        if (parseInt(localizedObj.hasBackToTopArrow)) {
            $.scrollUp({
                scrollText: '<i class="fa fa-angle-up"></i>',
                easingType: 'linear',
                scrollSpeed: 900,
                animation: 'fade'
            });
        }


        /*-------------------------------------
        ## search box click toggle
        -------------------------------------*/
        /*-------------------------------------
        ## search box click toggle
        -------------------------------------*/
        $('.top-search-form').each(function(index, el) {
            function toggleSearchInput(el) {
                $(el)
                    .find('input.search-input')
                    .animate({
                        width: ["toggle", "swing"],
                        height: ["toggle", "swing"],
                        opacity: "toggle"
                    }, 300, "linear")
            }

            $(el).find('.search-button').on('click', function(event) {
                event.preventDefault();
                event.stopPropagation()
                toggleSearchInput(el)
                $(el).find('a.search-close').toggle(100);
            })

            $(el).find('.search-close').on('click', function(event) {
                event.preventDefault();
                event.stopPropagation()
                toggleSearchInput(el);
                $(el).find('a.search-close').hide(100);
            })

        });




        /*-------------------------------------
        ## Counter
        -------------------------------------*/
        var counterContainer = $('.counter');
        counterContainer.each(function(index, el) {
            var counter_delay = $(el).data('delay') || 50;
            var counter_time = $(el).data('time') || 5000;
            var counter_option = {
                delay: counter_delay,
                time: counter_time
            }
            $(el).counterUp(counter_option);

        });

        /*-------------------------------------
        ## makebg
        -------------------------------------*/
        $('[data-make-bg]').each(function(e) {
            var img = $(this).data('make-bg');
            $(this).css({
                'background-image': 'url(' + img + ')',
                'background-repeat': 'no-repeat',
                'background-position': 'center',
                'background-size': 'cover',

            })
        });

        /*-------------------------------------
        MeanMenu activation code
        --------------------------------------*/
        $('.main-navigation').meanmenu({
            siteLogo: localizedObj.siteLogo,
            appendHtml: localizedObj.appendHtml,
            meanScreenWidth: localizedObj.meanWidth,
            meanRevealPosition: localizedObj.is_rtl ? "left" : "right",
        });

        $('.mean-nav .menu-item > a').on('click', function() {
            setTimeout(function() {
                $('.mean-bar .meanclose').trigger('click');
            }, 300)
        });

        /*-------------------------------------
        ## popup youtube video
        -------------------------------------*/
        var yPopup = $(".popup-youtube");
        if (yPopup.length) {
            yPopup.magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false
            });
        }

        /*-------------------------------------
        ## shop grid initialization
        -------------------------------------*/
        rdtheme_wc_scripts($);


    } // end onReadyScripts function ended



    function onLoadScripts() {

        $('#preloader').fadeOut('slow', function() {
            $(this).remove();
        });

        /**
         * activeHashMenu - for making menu link active in one page
         * 1. get all the anchor
         * 2. bind events for anchor click
         * 3. make clicked anchor active others inactive
         * 4. onscroll 
         * 
         */
        var activeHashMenu = {
            init: function() {
                this.initialValue();
                this.bindEvents();
                this.generateIds();
            },
            initialValue: function() {
                this.activeClass = 'current-hash-item';
                this.$menu = $('.main-navigation .menu');
                this.$navItems = this.$menu.find('a');
                this.ids = [];
                var scrollItems = [];
                this.$navItems.each(function() {
                    var attr = $(this).attr('href');
                    var has_attr = typeof attr !== typeof undefined && attr !== false;
                    var start_with_hash = has_attr && attr.startsWith('#')
                    if (start_with_hash) {
                        var item = $($(attr));
                        if (item.length && item.selector && item.selector.length > 2) {
                            scrollItems.push(item);
                        }
                    }
                });
                this.$scrollItems = scrollItems;
            },
            generateIds: function() {
                var ids = [];
                var self = this;
                this.$navItems.each(function() {
                    var hash = self.getHash($(this));
                    if (hash) {
                        ids.push(hash);
                    }
                })
                this.ids = ids;
            },
            bindEvents: function() {
                self = this;
                this.$navItems.on('click', function() {
                    self.classToggle($(this));
                })

                var lastId;
                var cur;
                if (this.$scrollItems.length) {
                    $(window).scroll(function() {
                        // Get container scroll position
                        // why 175 is working here
                        var fromTop = $(this).scrollTop() + 175;

                        var scrollPositions = self.$scrollItems.map(function(eachElm) {
                            if ($(eachElm).offset().top < fromTop)
                                return eachElm;
                        });
                        // remove undefined item
                        scrollPositions = scrollPositions.filter(function(item) {
                            return item;
                        })
                        if (scrollPositions.length) {
                            // last item from this array is our current position
                            cur = scrollPositions[scrollPositions.length - 1];
                            var id = cur && cur.length ? cur[0].id : "";
                            if (lastId !== id) {
                                lastId = id;
                                var current_item = self.$menu.find("[href=#" + id + "]");
                                self.classToggle(current_item);
                            }
                        }
                    });
                }

            },
            getHash: function($link) {
                if ($link.attr('href')) {
                    return $link.attr('href').split('#')[1];
                } else {
                    return '';
                }
            },
            classToggle: function(elm) {
                if (this.hasPosition(elm)) {
                    this.$menu.find('.' + this.activeClass).removeClass(this.activeClass);
                    elm.closest('li').addClass(this.activeClass);
                }
            },
            hasPosition: function(elm) {
                var bool = false;
                var linkHref = this.getHash($(elm));
                if (!linkHref) {
                    return false;
                }
                var target = $('#' + linkHref);
                return target ? true : false;
            },
        }
        activeHashMenu.init();


        /*-------------------------------------
        ## owl carousel (when initiate options using php)
        -------------------------------------*/

        if (typeof $.fn.owlCarousel == 'function') {
            $(".owl-custom-nav .owl-next").on('click', function() {
                $(this).closest('.owl-wrap').find('.owl-carousel').trigger('next.owl.carousel');
            });
            $(".owl-custom-nav .owl-prev").on('click', function() {
                $(this).closest('.owl-wrap').find('.owl-carousel').trigger('prev.owl.carousel');
            });
            $(".rt-owl-carousel").each(function() {
                var options = $(this).data('carousel-options');
                $(this).owlCarousel(options);
            });
        }

        /*-------------------------------------
         ## Blog masonry layout
         -------------------------------------*/
        if (typeof Isotope !== "undefined") {
            setTimeout(function() {
                var $grid = $('.masonry-grid').isotope({
                    itemSelector: '.masonry-grid-item',
                })
            }, 1200)
        }

        /**
         * Hover effect for service icon image change
         */
        function service_icon_hover_state(element) {
            $(element).hover(function() {
                $(this).find(".service-icon-image img:last").fadeToggle();
            });
        }
        service_icon_hover_state('.rtel-service-gallery2 .rtin-service-box');
        service_icon_hover_state('.rtel-service-gallery5 .rtin-service-box');
        service_icon_hover_state('.rtel-service-gallery7 .rtin-service-box');
        service_icon_hover_state('.service-box-layout4');
        service_icon_hover_state('.service-box-layout6');


        // just below line onLoadScripts fn ended
    }



    /*---------------------------------------------------------------
    ## loading all scripts after document ready
    ---------------------------------------------------------------*/

    $(document).ready(function() {
        onReadyScripts();
    })
    $(window).on('load', function() {
        onLoadScripts();
    })

    /*-------------------------------------
    ## elementor frontend hooks
    -------------------------------------*/
    $(window).on('elementor/frontend/init', function() {
        if (elementorFrontend.isEditMode()) {
            elementorFrontend.hooks.addAction('frontend/element_ready/widget', function() {
                onReadyScripts();
                onLoadScripts();
            });
        }
    });


    /*-------------------------------------
    ## for keeping same height widget
    -------------------------------------*/
    function sameHeight(selector) {
        var elements = $(selector);
        var max_height = 0;
        elements.each(function(index, el) {
            var height = $(el).height();
            if (height > max_height) {
                max_height = height;
            }
        });
        elements.height(max_height);

    }
    sameHeight('.currently-not-using');


    /*-------------------------------------
    ## making things square
    -------------------------------------*/
    $.fn.squareMaker = function() {
        this.each(function(index, el) {
            var width = $(el).width();
            $(el).height(width);
        });
        return this;
    };
    $('.rtel-team-gallery3 .rtin-team-layout3 .item-img').squareMaker();

    $('.el-padding-left-wrapper').find('.elementor-column-wrap').addClass('el-padding-left');
    $('.el-padding-right-wrapper').find('.elementor-column-wrap').addClass('el-padding-right');

})(jQuery);