program TabelPerkalianKombinasi;
uses crt;
var
  i, j: integer;
begin
  clrscr;
  
  // Menggunakan 'while' untuk angka 6
  i := 6;
  while i < 7 do
  begin
    for j := 0 to 6 do
    begin
      writeln(i, ' x ', j, ' = ', i * j);
    end;
    writeln('-------------------');
    i := i + 1;
  end;

  // Menggunakan 'for..downto do' untuk angka 7
  for i := 7 downto 7 do
  begin
    j := 0;
    repeat
      writeln(i, ' x ', j, ' = ', i * j);
      j := j + 1;
    until j > 6;
    writeln('-------------------');
  end;

  readln;
end.
