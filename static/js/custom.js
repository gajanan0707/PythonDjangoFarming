$(document).ready(function() {
 $('.form-signup').validate(
  {
    rules:{
        'username':{
            required:true,
            minlength:3

         },
         'first_name':{
            required:true,
            minlength:1

         },
         'last_name':{
            required:true,
            minlength:1

         },
         'email':{
            required:true,
            email:true

         },
         'password1':{
            required:true,
            minlength:8

         },
         'password2':{
            required:true,
            equalTo:'#id_password1'

         }
     },


     messages:{
        'username':{
            required:"username is required",
            minlength:"Please Enter at least 3 charcter"

            },

         'first_name':{
            required:"First name is required",
            minlength:"Please Enter at least 1 charcter"

            },

         'last_name':{
            required:"First name is required",
            minlength:"Please Enter at least 3 charcter"

            },

         'email':{
            required:"email id is required",
            email:"please Enter valid email"

            },
         'password1':{
            required:"password is required",
            minlength:"please enter at least 8 character"

             },

         'password2':{
            required:"please enter the confirm password",
            equalTo:"your password not matched"

            }

        },
     });

        $('#id_username').change(function(){
          var user_name =  $('#id_username').val();
          $.ajax({
              url: '/profiles/check-username/',
              data: { uname: user_name},
              type: json,
              success: function(response) {
                  console.log(response.status);
               },
               error: function(err){
                   alert(err);
               }
        });

   });

    $('#example').DataTable();
});
