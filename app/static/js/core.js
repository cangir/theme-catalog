

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

  new EasyMDE({
    autoDownloadFontAwesome: true,
    element: document.getElementById('input_content')
  });

  new EasyMDE({
    autoDownloadFontAwesome: true,
    element: document.getElementById('input_features')
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
    var $this = $('.go-to-top');

    $this.on("click", function (event) {
      event.preventDefault();
      $("html, body").animate({ scrollTop: 0 }, 600);
    });

    var go_to_top = function () {
      var current_windows_position = $(window).scrollTop();

      if (current_windows_position > 400) {
        $this.addClass("show");
      } else {
        $this.removeClass("show");
      }
    };

    go_to_top();

    $(window).scroll(function () {
      go_to_top();
    });
  }());



});

