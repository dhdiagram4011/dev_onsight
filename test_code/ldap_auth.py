#if get_result == 200:
#    print("login success")
#    ###kubectl set image deployment ...
#else:
#    print("login Failed...rollback start!")
    ##os.system('kubectl get pods')
    ##os.system('echo kubectl rollout ')


#if __name__ == "__main__":
#    rpldap="rpldap.rockplace.co.kr:636"
#    username="dohyoung.kim@rockplace.co.kr"
#    oudc="ou=People,dc=rockplace,dc=co,dc=kr"
#    bdn="dc=rockplace,dc=co,dc=kr"
#    password="rlaehgud2176"
#    user_dn="uid="+username+"oudc"
#    #user_dn:uid=dohyoung.kim,ou=People,dc=rockplace,dc=co,dc=kr
#    basedn="bdn"
#    connect=ldap.open(rpldap)
#    search_filter="uid"+username
#    try:
#            connect.bind_s(user_dn,password)
#            result=connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
#            connect.unbind_s()
#    except ldap.LDAPError:
#           connect.unbind.s()
#           print("authentication error")
