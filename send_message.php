<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input data
    $name = htmlspecialchars(strip_tags(trim($_POST['name'])));
    $email = htmlspecialchars(strip_tags(trim($_POST['email'])));
    $message = htmlspecialchars(strip_tags(trim($_POST['message'])));
    
    // Validate input
    if (!empty($name) && filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($message)) {
        // Set the recipient email address
        $to = "gundetisaiteja25@gmail.com"; // Change this to your email address
        $subject = "New Contact Form Submission from $name";
        
        // Create the email content
        $email_content = "Name: $name\n";
        $email_content .= "Email: $email\n\n";
        $email_content .= "Message:\n$message\n";

        // Set the email headers
        $headers = "From: $name <$email>";

        // Send the email
        if (mail($to, $subject, $email_content, $headers)) {
            // Email sent successfully
            echo "Thank you for contacting me, $name. I will get back to you soon!";
        } else {
            // Email sending failed
            echo "Oops! Something went wrong and I couldn't send your message.";
        }
    } else {
        // Invalid input
        echo "Please fill in all fields correctly.";
    }
} else {
    // Not a POST request
    echo "Invalid request.";
}
?>
