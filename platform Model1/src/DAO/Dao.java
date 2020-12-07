package DAO;

import java.sql.*;
import java.util.ArrayList;

import VO.CellLineCategory;
import VO.TumorTypeCategory;
import config.DBconfig;

public class Dao {

	
	public ArrayList<CellLineCategory> getData(String name){
		
		ArrayList<CellLineCategory> cellLineCategories=null;
		
		try {
			Class.forName("com.mysql.jdbc.Driver");
			Connection conn = DriverManager.getConnection(DBconfig.url, DBconfig.id, DBconfig.password);
			Statement stmt = conn.createStatement();
			String sql=String.format("select * from cell_line_category where id=(select id from tumor_type_category where name = '%s')", name);
			ResultSet rs = stmt.executeQuery(sql);
			cellLineCategories = new ArrayList<CellLineCategory>();
			while(rs.next()) {
				CellLineCategory cellLineCategory = new CellLineCategory();
				String tumorName = rs.getString("name");
				cellLineCategory.setName(tumorName);
				cellLineCategories.add(cellLineCategory);
			}
		}
		catch(Exception e) {
			System.out.println(e);
		}
		return cellLineCategories;
	}
}
