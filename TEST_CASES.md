# SafeRoute AI - Test Cases

## Route Navigation

| ID | Test Case | Expected Result |
|------|------|------|
| TC001 | Enter destination | Route generated |
| TC002 | Select safest route | Safe route displayed |
| TC003 | Travel during night hours | High-risk warning shown |
| TC004 | Enter invalid destination | Error message displayed |

---

## GPS

| ID | Test Case | Expected Result |
|------|------|------|
| TC005 | Enable GPS | Location detected |
| TC006 | Disable GPS | User prompted to enable GPS |

---

## Risk Prediction

| ID | Test Case | Expected Result |
|------|------|------|
| TC007 | Request risk score | Score returned |
| TC008 | High-risk area detected | Alert generated |
| TC009 | Safe area detected | Safe status displayed |

---

## Incident Reporting

| ID | Test Case | Expected Result |
|------|------|------|
| TC010 | Submit incident | Report saved |
| TC011 | Missing information | Validation error displayed |

---

## Emergency SOS

| ID | Test Case | Expected Result |
|------|------|------|
| TC012 | Activate SOS | Alert sent |
| TC013 | GPS unavailable | Error displayed |

---

## Authentication

| ID | Test Case | Expected Result |
|------|------|------|
| TC014 | Register new user | Account created |
| TC015 | Login with valid credentials | Login successful |
| TC016 | Login with invalid credentials | Error message displayed |
