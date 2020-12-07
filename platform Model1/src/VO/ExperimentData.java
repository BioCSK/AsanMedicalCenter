package VO;

import java.sql.Date;

public class ExperimentData {

	private Long id;
	
	public Long getId() {
		return id;
	}



	public void setId(Long id) {
		this.id = id;
	}



	public double getTumorsize() {
		return tumorsize;
	}



	public void setTumorsize(double tumorsize) {
		this.tumorsize = tumorsize;
	}



	public Integer getTime() {
		return time;
	}



	public void setTime(Integer time) {
		this.time = time;
	}



	public String getGroup() {
		return group;
	}



	public void setGroup(String group) {
		this.group = group;
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



	public ExperimentMetaData getExperimentMetaData() {
		return experimentMetaData;
	}



	public void setExperimentMetaData(ExperimentMetaData experimentMetaData) {
		this.experimentMetaData = experimentMetaData;
	}



	private double tumorsize;
	
	private Integer time;
	
	private String group;
	
	private Date createdAt;
	
	private String createdBy;
	
	
	
	private ExperimentMetaData experimentMetaData;
	
	
}
