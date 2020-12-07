package VO;

import java.sql.Date;
import java.util.List;

public class CellLineCategory {
	
	private Long id;
	
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

	public TumorTypeCategory getTumorTypeCategory() {
		return tumorTypeCategory;
	}

	public void setTumorTypeCategory(TumorTypeCategory tumorTypeCategory) {
		this.tumorTypeCategory = tumorTypeCategory;
	}

	public List<ExperimentMetaData> getExperimentMetaData() {
		return experimentMetaData;
	}

	public void setExperimentMetaData(List<ExperimentMetaData> experimentMetaData) {
		this.experimentMetaData = experimentMetaData;
	}

	private String name;
	
	private String description;
	
	private Date createdAt;
	
	private String createdBy;
	
	private TumorTypeCategory tumorTypeCategory;
	
	private List<ExperimentMetaData> experimentMetaData;
	
}
