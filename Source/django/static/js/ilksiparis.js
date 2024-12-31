$(document).ready(function () {
    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

    if ($('.modal-body').length) {
        $('.modal-body .select').select2({
          language: 'tr',
          placeholder: '---------',
          width: '100%',
          dropdownParent: $('.modal-body')
        });
      } else {
        $('select').select2({
          language: 'tr',
          placeholder: '---------',
          width: '100%'
        });
      }
});

