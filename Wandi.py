program DeretAngkaDenganTMemo;
uses crt, Forms, StdCtrls, Controls, Classes;

type
  TForm1 = class(TForm)
    Memo1: TMemo;
    procedure TampilkanDeretAngka;
  end;

var
  Form1: TForm1;

procedure TForm1.TampilkanDeretAngka;
var
  i, sum, addend: Integer;
  output: String;
begin
  sum := 1; // Karena kita mulai dari 1+1
  addend := 0;
  output := '';

  // Menggunakan perulangan for untuk menghitung deret angka
  for i := 1 to 5 do
  begin
    case i of
      1: addend := 1;
      2: addend := 4;
      3: addend := 2;
      4: addend := 7;
      5: addend := 3;
    end;

    sum := sum + addend;

    // Menambahkan hasil ke string output
    output := output + IntToStr(sum) + ' ';
  end;

  // Menggunakan perulangan while untuk menambahkan hasil ke TMemo
  i := 1;
  while i <= Length(output) do
  begin
    Memo1.Text := Memo1.Text + output[i];
    i := i + 1;
  end;
end;

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Form1.TampilkanDeretAngka;
  Application.Run;
end.
