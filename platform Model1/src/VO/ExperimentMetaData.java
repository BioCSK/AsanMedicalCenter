package VO;

import java.sql.Date;
import java.util.List;

public class ExperimentMetaData {
	
	
	private Long id;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Date getExperimentDate() {
		return experimentDate;
	}

	public void setExperimentDate(Date experimentDate) {
		this.experimentDate = experimentDate;
	}

	public CellLineCategory getCellLineCategory() {
		return cellLineCategory;
	}

	public void setCellLineCategory(CellLineCategory cellLineCategory) {
		this.cellLineCategory = cellLineCategory;
	}

	public List<ExperimentData> getExperimentData() {
		return ExperimentData;
	}

	public void setExperimentData(List<ExperimentData> experimentData) {
		ExperimentData = experimentData;
	}

	private Date experimentDate; 
	
	private CellLineCategory cellLineCategory;
	
	private List<ExperimentData> ExperimentData;

}
