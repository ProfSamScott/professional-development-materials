<!DOCTYPE html>
<!--
Counting exercise solution. Exercise 3.9 number 1.
Sam Scott, 2014
-->
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Counting</title>
    </head>
    <body>
        <?php
        if (isset($_GET["start"])) {
            $start = clean($_GET["start"]);
        } else {
            $start = 1;
            echo "<p>WARNING: Default value used for start parameter.";
        }
        if (isset($_GET["end"])) {
            $end = clean($_GET["end"]);
        } else {
            $end = 1000;
            echo "<p>WARNING: Default value used for end parameter.";
        }
        if (isset($_GET["by"])) {
            $by = clean($_GET["by"]);
        } else {
            $by = 1;
            echo "<p>WARNING: Default value used for 'by' parameter.";
        }
        $error = false;
        if (!is_numeric($start) || $start < -1000 || $start > 1000) {
            echo "<p>ERROR: Start param must be an integer between -1000 and 1000.</p>";
            $error = true;
        }
        if (!is_numeric($end) || $end < -1000 || $end > 1000) {
            echo "<p>ERROR: End param must be an integer between -1000 and 1000.</p>";
            $error = true;
        }
        if (!is_numeric($by) || $by < -1000 || $by > 1000) {
            echo "<p>ERROR: Count by param must be an integer between -1000 and 1000.</p>";
            $error = true;
        }
        if (!$error)
            for ($i = $start; $i <= $end; $i+=$by)
                echo "<p>$i</p>";
        ?>
    </body>
</html>
<?php
function clean($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>