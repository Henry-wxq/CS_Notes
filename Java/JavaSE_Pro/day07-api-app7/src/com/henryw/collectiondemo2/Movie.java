package com.henryw.collectiondemo2;

public class Movie {
    private String name;
    private double score;
    private String director;

    public Movie() {
    }

    public Movie(String name, double score, String director) {
        this.name = name;
        this.score = score;
        this.director = director;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    @Override
    public String toString() {
        return "Movie{" +
                "name='" + name + '\'' +
                ", score=" + score +
                ", director='" + director + '\'' +
                '}';
    }
}
