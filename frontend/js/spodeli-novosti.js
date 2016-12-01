$(document).ready(function () {
  $('#uspesnoDodaden').hide();
  $('#neuspesnoDodaden').hide();
  $('#uspesnoIspratena').hide();
  $('#neuspesnoIspratena').hide();

  $.ajax({
           type: "GET",
           url: 'http://localhost:8000/subscriber'
         }).always(function (res) {
    if (res.status) {
      $('#uspesnoIspratena').hide();
      $('#neuspesnoIspratena').show();
      $('#neuspesnoIspratena').html(res.responseJSON.description)
    } else {
      $('#brKorisnici').html(res.length)
    }
  });

  $('#newsletter-send').submit(function (event) {
    event.preventDefault();

    var data = {
      subject: $('#subject').val(),
      body: $('#body').val()
    };

    if (data.subject === '') {
      delete data.subject
    }
    if (data.body === '') {
      delete data.body
    }

    $.ajax({
                               type: "POST",
                               url: 'http://localhost:8000/send',
                               data: JSON.stringify(data)
                             }).always(function (res) {
      if (res.status) {
        $('#uspesnoIspratena').hide();
        $('#neuspesnoIspratena').show();
        $('#neuspesnoIspratena').html(res.responseJSON.description)
      } else {
        $('#uspesnoIspratena').show();
        $('#neuspesnoIspratena').hide();
        $('#uspesnoIspratena').html(res.description);
      }
      console.log(res)
    })
  });

  $('#add').submit(function (event) {
    event.preventDefault();

    var data = {
      name: $('#name').val(),
      email: $('#email').val()
    };

    if (data.name === '') {
      delete data.name
    }

    $.ajax({
             type: "POST",
             url: 'http://localhost:8000/subscriber',
             data: JSON.stringify(data)
           }).always(function (res) {
      if (res.status) {
        $('#uspesnoDodaden').hide();
        $('#neuspesnoDodaden').show();
        $('#neuspesnoDodaden').html(res.responseJSON.description);
      } else {
        $('#uspesnoDodaden').show();
        $('#neuspesnoDodaden').hide();
        $('#uspesnoDodaden').html(res.description)
      }
    });
  })
});