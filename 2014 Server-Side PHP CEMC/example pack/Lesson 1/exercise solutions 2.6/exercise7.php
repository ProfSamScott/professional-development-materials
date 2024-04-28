<!DOCTYPE html>
<!--
Solution: Using PHP to generate a multiplication table. Compare this to
MultiplicationTablePHP2.php. Which is better?

Sam Scott, March 12, 2012.
-->
<html>
    <head>
        <?php
            $ROWS = 10;
            if(isset($_GET["rows"]))
                $ROWS=$_GET["rows"];
            $COLS = 10;
            if(isset($_GET["cols"]))
                $COLS=$_GET["cols"];
        ?>    
        <link rel="stylesheet" type="text/css" href="css/multiplicationtable.css">
        <title>PHP-Generated Multiplication Table</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
        <div>
            <h1>PHP-Generated Multiplication Table</h1>
            <?php
                echo "<table><tr>";
                
                // HEADER ROW
                echo "<tr><td>X</td>";
                for ($col = 1; $col<=$COLS; $col++)
                    echo "<td class='headCell'>".$col."</td>";
                echo "</tr>";
                
                // BODY OF TABLE
                for ($row = 1; $row<=$ROWS; $row++) {
                    echo "<tr><td class='headCell'>".$row."</td>";
                    for ($col = 1; $col<=$COLS; $col++) {
                        echo "<td class='cell'>".($row*$col)."</td>";
                    }
                    echo "</tr>";
                }
                        
                echo "</table>";
            ?>
            <p>* Use parameters "rows" and "cols" to change the size of the table.</p>
        </div>
    </body>
</html>
