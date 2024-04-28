<!DOCTYPE html>
<!--
An example of server-side data validation. Use with serverSideVal.html to see
it in action.
Sam Scott, Sheridan college, 2014.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Server Side Data Validation</title>
        <style type="text/css">
            .error { color:red;}
            .good {color:green;}
        </style>
    </head>
    <body>
        <h1>Server Side Data Validation</h1>
        <?php
        // FIRST PARAMETER
        if (isset($_GET["even"])) {
            $even = clean($_GET["even"]);
            if (empty($even))
                echo "<p class='error'>First parameter was empty. Please <a href='serverSideVal.html'>try again.</a></p>";
            else if (!is_numeric($even))
                echo "<p class='error'>First parameter was not a number. Please <a href='serverSideVal.html'>try again.</a></p>";
            else if ($even % 2 == 0 && $even <= 100 && $even >= 0)
                echo "<p class='good'>First parameter is ok.</p>";
            else
                echo "<p class='error'>First parameter should be even and between 0 and 100.</p>";
        } else {
            echo "<p class='error'>First parameter missing. Please <a href='serverSideVal.html'>try again.</a></p>";
        }
        // SECOND PARAMETER
        if (isset($_GET["code"])) {
            $code = clean($_GET["code"]);
            if (strlen($code) < 1 || strlen($code) > 10)
                echo "<p class='error'>Second parameter must be 1 to 10 characters long. Please <a href='serverSideVal.html'>try again.</a></p>";
            else
                echo "<p class='good'>Second parameter is ok.</p>";
        } else {
            echo "<p class='error'>Second parameter missing. Please <a href='serverSideVal.html'>try again.</a></p>";
        }
        // THIRD PARAMETER
        if (isset($_GET["variableName"])) {
            $varName = clean($_GET["variableName"]);
            if (preg_match('/^[a-zA-Z][a-zA-Z0-9_]*/', $varName) == 0)
                echo "<p class='error'>Third parameter must be a legal variable name. Please <a href='serverSideVal.html'>try again.</a></p>";
            else
                echo "<p class='good'>Third parameter is ok.</p>";
        } else {
            echo "<p class='error'>Third parameter missing. Please <a href='serverSideVal.html'>try again.</a></p>";
        }
        ?>
    </body>
</html>
<?php

// Function to clean up a data string
// From w3schools.com
function clean($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>