<html>
    <head>
        <meta charset="UTF-8"/>
    </head>
</html>
<body>
<form action="/add" method="POST">
	<input type="text" required size="20" placeholder="Телефонный номер" maxlength="14" name="phone">
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