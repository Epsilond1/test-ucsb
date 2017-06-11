<p>Содержимое базы данных</p>
<table border="1">
%for row in rows:
  <tr>
  %for r in row:
    <td>{{r}}</td>
  %end
  </tr>
%end
</table>

<form action="/">
	<input type="submit" name="back" value="back...">
</form>