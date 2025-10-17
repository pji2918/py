region = ["한국", "미국", "중국", "필리핀"]
captial = ["서울", "워싱턴 D.C.", "베이징", "마닐라"]
area = [100.2, 9834, 9597, 300]

city_info = list(zip(region, captial, area))
city_region, city_capital, city_area = zip(*city_info)

max_area = max(city_area)
max_area_idx = city_area.index(max_area)
print(f"최대 인구 도시: {city_region[max_area_idx]}, 인구 수: {max_area}")
