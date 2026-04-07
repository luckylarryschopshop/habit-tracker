# Product Requirements Document (PRD) - Habit Tracker Web App

## 1. Overview

This document outlines the requirements for a habit tracker web application. The application allows users to track daily habits, mark them as complete, view their streaks, and get a weekly overview of their progress. The application will be built using a FastAPI backend and an HTML frontend, with data stored in JSON format.

## 2. Features

### 2.1 Add Habits
- Users can add new habits by providing a name and optional description.
- Each habit is stored with a unique identifier.
- Users can edit or delete habits after they are added.

### 2.2 Mark Complete Per Day
- Users can mark a habit as complete for the current day.
- Each habit has a daily status that can be marked as complete or incomplete.
- The app tracks the date for each habit completion.

### 2.3 View Streaks
- Users can view their current streak for each habit.
- A streak is calculated as the number of consecutive days a habit has been marked as complete.
- The streak resets if a day is missed.

### 2.4 Weekly Overview
- Users can view a summary of their habit progress for the current week.
- The overview includes a calendar-style view or a list of daily habit status.
- Users can navigate between weeks to review past progress.

## 3. Data Storage

- All habit data is stored in a JSON file.
- The JSON structure includes:
  - Habit ID
  - Habit name and description
  - Daily completion status
  - Streak count
  - Weekly progress data

## 4. User Interface

- The frontend is built using HTML and basic CSS.
- Users interact with the app through a simple and intuitive interface.
- The interface includes:
  - A form to add or edit habits
  - A daily habit tracker
  - A section to view current streaks
  - A weekly overview dashboard

## 5. Backend

- The backend is built using FastAPI.
- It provides RESTful endpoints for:
  - Creating and updating habits
  - Marking habits as complete
  - Retrieving habit data
  - Fetching streak and weekly data
- The backend handles all data operations and ensures data consistency.

## 6. Non-Functional Requirements

- The app must be responsive and work on desktop and mobile devices.
- Data must be persisted across sessions using the JSON storage.
- The app must be secure and prevent unauthorized access to user data.

## 7. Assumptions

- Users will not share their JSON data with others.
- The app is intended for personal use only.
- The JSON file will be stored locally on the user’s device.

## 8. Success Criteria

- Users can successfully add, track, and review their habits.
- The app accurately calculates and displays streaks and weekly progress.
- The app functions reliably with no data loss or corruption.