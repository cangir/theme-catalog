

/**
 *
 */
$(document).ready(function () {

  const DIV_CARD = 'div.card';

  /** Initialize tooltips */
  $('[data-toggle="tooltip"]').tooltip();

  /** Initialize popovers */
  $('[data-toggle="popover"]').popover({
    html: true
  });

  /** Function for collapse card */
  $('[data-toggle="card-collapse"]').on('click', function (e) {
    let $card = $(this).closest(DIV_CARD);

    $card.toggleClass('card-collapsed');

    e.preventDefault();
    return false;
  });

  $.gdprcookie.init();

  // Go to Top
  var go2TopShowHide = (function () {
    var $this = $('.js-go-to');

    $this.on("click", function (event) {
      event.preventDefault();
      $("html, body").animate({ scrollTop: 0 }, 600);
    });

    var go2TopOperation = function () {
      var CurrentWindowPosition = $(window).scrollTop();

      if (CurrentWindowPosition > 400) {
        $this.addClass("show");
      } else {
        $this.removeClass("show");
      }
    };

    go2TopOperation();

    $(window).scroll(function () {
      go2TopOperation();
    });
  }());



});

