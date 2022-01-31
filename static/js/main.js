$.fn.Set_Input_Direction = function()
{
    $(this).off('keypress').on('keypress',function(e){
        _This = $(this);
        setTimeout(function()
        {
            if(_This.val().length > 1)
            {
                return;
            }
            else
            {
                var RTL_Regex = /[\u0591-\u07FF\uFB1D-\uFDFD\uFE70-\uFEFC]/;
                var isRTL     = RTL_Regex.test(String.fromCharCode(e.which));
                var Direction = isRTL ? 'rtl' : 'ltr';
                _This.css({'direction' : Direction});
            }
        });
    });
};

$('input').Set_Input_Direction();
$('textarea').Set_Input_Direction();

$('.addToFav').on('click', function (){
    $(this).toggleClass('active');
})

$(document).ready(function() {
  //change colour when radio is selected
  $('.selector input').change(function() {
    // Only remove the class in the specific `box` that contains the radio
    $('.selector.highlight').removeClass('highlight');
    let inpSelector = $(this).attr('data-selector');
    $(inpSelector).addClass('highlight');
  });
});
