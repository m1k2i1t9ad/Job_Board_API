# Job Board Platform

A backend job board platform built with Django and Django REST Framework. Employers can post job listings, and job seekers can search and apply for jobs. The platform includes features like user authentication (JWT), media storage (Cloudinary), pagination, and testing.

---

## Features

- **User Roles**:
  - **Employers**: Can post job listings and view applications.
  - **Job Seekers**: Can search for jobs, upload resumes, and apply for jobs.

- **Job Listings**:
  - Employers can create, update, and delete job listings.
  - Job seekers can view active job listings.

- **Job Applications**:
  - Job seekers can apply to job listings.
  - Employers can track the status of applications (Pending, Accepted, Rejected).

- **Authentication**:
  - JWT (JSON Web Tokens) for secure user authentication.
  - Token refresh mechanism for extended sessions.

- **Media Storage**:
  - Resumes are stored using **Cloudinary** for scalable and secure file storage.

API Endpoints
Authentication
Login: POST /api/token/

Refresh Token: POST /api/token/refresh/

Users
Employer Profile: GET /api/users/employer-profile/

Job Seeker Profile: GET /api/users/job-seeker-profile/

Jobs
List/Create Job Listings: GET /api/jobs/listings/, POST /api/jobs/listings/

Retrieve/Update/Delete Job Listing: GET /api/jobs/listings/<id>/, PUT /api/jobs/listings/<id>/, DELETE /api/jobs/listings/<id>/

Apply for a Job: POST /api/jobs/listings/<id>/apply/
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m1k2i1t9ad/Job_Board_API.git
   cd jobboard
