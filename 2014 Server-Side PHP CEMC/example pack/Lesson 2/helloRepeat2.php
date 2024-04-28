<!DOCTYPE html>
<?php
/* Example Hello World program with Parameters, but with the HTML separated
 * from the PHP.
 * 
 * Sam Scott, March 2012
 */
?>
<html>
    <head>
        <meta charset='UTF-8'>
        <title>Hello Client Repeat</title>
    </head>
    <body>
        <?php
        if (isset($_GET['numHellos']))
            $n = $_GET['numHellos'];
        else
            $n = 1;
        for ($i = 0; $i < $n; $i++) { 
            ?>
            <p>Hello, World!</p>
            <?php
        }
        ?>
    </body>
</html>

