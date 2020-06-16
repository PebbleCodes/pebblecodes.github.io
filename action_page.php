<?php
    $name = $_POST['name'];
    $vistor_email = $_POST['email'];
    $message = $_POST['message'];

    $email_from = 'contact@pebblecodes.com';
    $email_subject = "New Form Submission";
    $email_body = "User Name: $name\n". 
                    "User Email: $visitor_email\n". 
                        "User Message: $message\n";
    $to = "mark@pebblecodes.com";
    $headers = "From: $email_from \r\n";
    $headers .= "Reply-To: $visitor_email \r\n";
    mail($to,$message,$email_body,$headers);
    header("Location: contact.html");
?>