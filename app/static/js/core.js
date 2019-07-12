

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

  $('.toast').toast('show');

  $.gdprcookie.init();

  $('#select_category').selectize({
    create: true,
    placeholder: "Please select ..."
  });

  $('#select_tag').selectize({
    create: true,
    placeholder: "Please select ..."
  });

  $('#select_license_type').selectize({
    create: true,
    placeholder: "Please select ...",
    maxItems: 1
  });

  $('#select_theme_author').selectize({
    create: true,
    placeholder: "Please select ...",
    maxItems: 1
  });

  new EasyMDE({
    autoDownloadFontAwesome: true,
    element: document.getElementById('input_content')
  });

  function readImagePreviewURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $('#image_preview_img').attr('src', e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  $('#image_preview').change(function () {
    readImagePreviewURL(this);
  });

  function readImageScreenshotURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $('#image_screenshot_img').attr('src', e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  $('#image_screenshot').change(function () {
    readImageScreenshotURL(this);
  });

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

