package VO;

import java.sql.Date;
import java.util.List;

public class TumorTypeCategory {

	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public String getCreatedBy() {
		return createdBy;
	}

	public void setCreatedBy(String createdBy) {
		this.createdBy = createdBy;
	}

	public List<CellLineCategory> getCellLineCategory() {
		return cellLineCategory;
	}

	public void setCellLineCategory(List<CellLineCategory> cellLineCategory) {
		this.cellLineCategory = cellLineCategory;
	}

	private Long id;
	
	private String name;
	
	private String description;
	
	private Date createdAt;
	
	private String createdBy;

	private List<CellLineCategory> cellLineCategory;



}
