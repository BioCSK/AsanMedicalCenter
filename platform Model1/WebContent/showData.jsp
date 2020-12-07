<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="DAO.Dao" %>
<%@ page import="VO.*" %>  
<%@ page import="java.util.*" %>  
<%
	String tumorType = request.getParameter("tumorType");
	Dao dao = new Dao();
	ArrayList<CellLineCategory> cellLineCategories = dao.getData(tumorType);
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<ul>
<%
	for(CellLineCategory clc : cellLineCategories){
%>
	<li><%=clc.getName() %></li>
<% 
	} 
%>
</ul>
</body>
</html>