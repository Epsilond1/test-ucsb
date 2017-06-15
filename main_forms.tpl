<html>
    <head>
        <meta charset="UTF-8"/>
    </head>
<body>
<form action="/add" method="POST">
	<input type="text" required size="20" placeholder="+7(343)111-33-44" maxlength="14" name="phone">
	<br>
	<input type="text" required size="20" placeholder="Иван" maxlength="20" name="name">
	<br>
	<input type="submit" name="add" value="add to DB">
</form>

<form action="/show" method="GET">
    <input type="submit" name="print" value="print rows DB">
</form>
</body>
</html>