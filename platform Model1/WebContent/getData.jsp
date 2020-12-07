<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="showData.jsp" method="GET">
        <!--보고싶은 암종별 선택하면 무슨 세포주에 해당되는 데이터가 있는지 -->
    <label for="1">암종류 선택</label>
    <select id="1" name="tumorType">
        <option value= "none" selected >SelectTumorType</option>
        <option value="Colon">Colon</option>
        <option value="Prostate">Prostate</option>
        <option value="Breast">Breast</option>
        <option value="Cervical">Cervical</option>
        <option value="Gastric">Gastric</option>
        <option value="HeadAndNeck">HeadAndNeck</option>
        <option value="Liver">Liver</option>
        <option value="Lung">Lung</option>
        <option value="Lymphoma">Lymphoma</option>
        <option value="Melanoma">Melanoma</option>
        <option value="Ovary">Ovary</option>
        <option value="Pancreas">Pancreas</option>
        <option value="SynivialSarcoma">SynivialSarcoma</option> 
    </select>
    <input type="submit" value="Submit">
    </form>
</body>
</html>