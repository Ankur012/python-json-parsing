import json
with open("uvsvn.json") as json_data:
    d = json.load(json_data)
#    print(d)
#    print d["start_time"]
    s_time = d["start_time"]
    e_time = d["end_time"]
    job_id = d["id"]
    print "job_id:" + job_id
    print "Total:" + "start time:" + s_time
    print "Total:" + "end time:" + e_time
    print "\n"
    phase_list = d["phase_list"]
    for item in phase_list:
#      print item["phase_name"]
      p_name = item["phase_name"]
      phase_status = item["actions"]
      for item in phase_status:
 #       print item["status"]
        s_name = item["status"]
        t_name = item["timestamp"]
  #      print item["timestamp"]
        print p_name + ": " +s_name+ ": "+t_name
#    print d["phase_list"]
