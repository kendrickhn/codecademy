# Warby Parker Customer Journey Insights

## 1. Quiz Funnel Analysis

| Question                             | Response Count | Drop-off Rate |
|--------------------------------------|----------------|---------------|
| 1. What are you looking for?         | 500            | -             |
| 2. What's your fit?                  | 475            | 5%            |
| 3. Which shapes do you like?         | 380            | 20%           |
| 4. Which colors do you like?         | 361            | 5%            |
| 5. When was your last eye exam?      | 270            | 25%           |

**Observations:**

- **Initial Engagement:** All 500 users responded to the first question, indicating strong initial interest.
- **Progressive Drop-off:** The most significant decreases occur between questions 2 and 3 (20%) and questions 4 and 5 (25%).

**Insights:**

- **Complexity and Sensitivity:** The higher drop-off rates at questions 3 and 5 suggest that users may find questions about personal preferences (shapes) and personal health information (eye exams) either too complex or intrusive. Simplifying these questions or providing context about their importance could improve completion rates.

## 2. Home Try-On and Purchase Conversion Analysis

| Number of Pairs | Users Started Quiz | Home Try-On Participants | Purchases Made | Try-On Conversion Rate | Purchase Conversion Rate |
|-----------------|--------------------|--------------------------|----------------|------------------------|--------------------------|
| 3 pairs         | 379                | 379                      | 201            | 100%                   | 53%                      |
| 5 pairs         | 371                | 371                      | 294            | 100%                   | 79%                      |

**Observations:**

- **Try-On Participation:** All users who reached the Home Try-On stage participated, indicating the program's appeal.
- **Purchase Rates:** Users who tried 5 pairs had a higher purchase rate (79%) compared to those who tried 3 pairs (53%).

**Insights:**

- **Increased Options Lead to Higher Purchases:** Offering more frames for trial correlates with higher purchase rates. This suggests that providing a broader selection may help customers find a pair they like, increasing the likelihood of purchase.

## Recommendations

- **Optimize Quiz Design:** Review and possibly rephrase or simplify questions 3 and 5 to reduce drop-off rates. Providing explanations for why certain information is requested may also help.
- **Enhance Home Try-On Program:** Consider promoting the 5-pair option more prominently, as it is associated with higher conversion rates.
- **Personalized Follow-Ups:** Implement targeted follow-up communications for users who drop off at specific quiz stages or do not proceed to purchase after the Home Try-On, addressing potential concerns or offering assistance.



# CoolTShirts Marketing Attribution Report

This report analyzes user behavior on CoolTShirts' website to evaluate the performance of different marketing campaigns. The goal is to determine which campaigns contribute most to user engagement and conversions, using both **first-touch** and **last-touch** attribution models.

---

## Campaign & Source Overview

**Query:**

```sql
SELECT COUNT(DISTINCT utm_campaign),
       COUNT(DISTINCT utm_source)
FROM page_visits;


**Result:**

| Campaigns | Sources |
|-----------|---------|
| 8         | 6       |

**Query:**

```sql
SELECT DISTINCT utm_campaign, utm_source
FROM page_visits;
```

**Result:**

| utm_campaign                          | utm_source |
|--------------------------------------|------------|
| getting-to-know-cool-tshirts         | nytimes    |
| weekly-newsletter                    | email      |
| ten-crazy-cool-tshirts-facts         | buzzfeed   |
| retargetting-campaign                | email      |
| retargetting-ad                      | facebook   |
| interview-with-cool-tshirts-founder  | medium     |
| paid-search                          | google     |
| cool-tshirts-search                  | google     |

---

## Website Journey

**Query:**

```sql
SELECT DISTINCT page_name
FROM page_visits;
```

**Result:**

- `1 - landing_page`
- `2 - shopping_cart`
- `3 - checkout`
- `4 - purchase`

---

## First-Touch Attribution

**Query:**

```sql
WITH first_touch AS (
  SELECT user_id, MIN(timestamp) AS first_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT pv.utm_campaign, COUNT(*) AS first_touch_count
FROM first_touch ft
JOIN page_visits pv
  ON ft.user_id = pv.user_id AND ft.first_touch_at = pv.timestamp
GROUP BY pv.utm_campaign;
```

**Top Campaigns by First Touch:**

| utm_campaign                          | first_touch_count |
|--------------------------------------|--------------------|
| interview-with-cool-tshirts-founder  | 622                |
| getting-to-know-cool-tshirts         | 612                |
| ten-crazy-cool-tshirts-facts         | 576                |
| cool-tshirts-search                  | 169                |

---

## Last-Touch Attribution

**Query:**

```sql
WITH last_touch AS (
  SELECT user_id, MAX(timestamp) AS last_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT pv.utm_campaign, COUNT(*) AS last_touch_count
FROM last_touch lt
JOIN page_visits pv
  ON lt.user_id = pv.user_id AND lt.last_touch_at = pv.timestamp
GROUP BY pv.utm_campaign;
```

**Top Campaigns by Last Touch:**

| utm_campaign                          | last_touch_count |
|--------------------------------------|------------------|
| weekly-newsletter                    | 692              |
| retargetting-ad                      | 443              |
| paid-search                          | 238              |
| getting-to-know-cool-tshirts         | 232              |
| ten-crazy-cool-tshirts-facts         | 190              |
| interview-with-cool-tshirts-founder  | 184              |

---

## Purchase Attribution

### Total Purchases

**Query:**

```sql
SELECT COUNT(DISTINCT user_id) AS total_purchase
FROM page_visits
WHERE page_name = '4 - purchase';
```

**Result:** `361` purchases

---

### Last-Touch Attribution for Purchases

**Query:**

```sql
WITH last_touch AS (
  SELECT user_id, MAX(timestamp) AS last_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT pv.utm_campaign, COUNT(*) AS purchase_last_touch
FROM last_touch lt
JOIN page_visits pv
  ON lt.user_id = pv.user_id AND lt.last_touch_at = pv.timestamp
WHERE page_name = '4 - purchase'
GROUP BY pv.utm_campaign;
```

**Result:**

| utm_campaign                          | purchase_last_touch |
|--------------------------------------|----------------------|
| retargetting-campaign                | 167                  |
| retargetting-ad                      | 112                  |
| paid-search                          | 54                   |
| getting-to-know-cool-tshirts         | 9                    |
| ten-crazy-cool-tshirts-facts         | 9                    |
| interview-with-cool-tshirts-founder  | 7                    |

---

## Recommendation: Campaigns to Reinforce

Based on the above metrics, CoolTShirts should consider reinvesting in the following 5 campaigns:

1. **interview-with-cool-tshirts-founder**  
   → Highest first-touch count + consistent presence in last-touch  
2. **retargetting-campaign**  
   → Strongest performance in driving purchases (167)  
3. **retargetting-ad**  
   → Great in both last-touch and conversions  
4. **paid-search**  
   → Balanced and reliable conversion support  
5. **getting-to-know-cool-tshirts**  
   → High first-touch and moderate last-touch/purchase performance

These campaigns demonstrate the strongest engagement and ROI potential across the funnel.
```