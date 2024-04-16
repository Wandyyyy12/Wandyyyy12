program PenjumlahanDeretMemo;
uses Forms, StdCtrls;

var
  Form: TForm;
  Memo: TMemo;
  n1, n2, n3, n4, n5, n6: integer;

begin
  Application.Initialize;
  Form := TForm.Create(nil);
  Memo := TMemo.Create(Form);
  Memo.Parent := Form;
  Memo.Align := alClient;
  Form.Show;

  n1 := 1 + 1; // Hasil dari 1+1
  Memo.Lines.Add('(' + IntToStr(n1) + ')');
  
  n2 := n1 + 4; // Menambahkan 4 ke hasil sebelumnya
  Memo.Lines.Add('(' + IntToStr(n2) + ')');
  
  n3 := n2 + 2; // Menambahkan 2 ke hasil sebelumnya
  Memo.Lines.Add('(' + IntToStr(n3) + ')');
  
  n4 := n3 + 7; // Menambahkan 7 ke hasil sebelumnya
  Memo.Lines.Add('(' + IntToStr(n4) + ')');
  
  n5 := n4 + 3; // Menambahkan 3 ke hasil sebelumnya
  Memo.Lines.Add('(' + IntToStr(n5) + ')');
  
  n6 := n5 + 3; // Menambahkan 3 ke hasil sebelumnya
  Memo.Lines.Add('(' + IntToStr(n6) + ')');

  Application.Run;
end.
