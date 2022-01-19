package s.demo;

import com.opensymphony.xwork2.ActionSupport;

//import org.apache.log4j.LogManager;
//import org.apache.log4j.Logger;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class UserAction extends ActionSupport {
    private static final long serialVersionUID = -1417237614181805435L;
    private static final Logger logger = LogManager.getLogger(UserAction.class);

    private String name;
    private String password;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }



    /**
     * 跳转到登录界面
     * @return
     */
    public String login_input() {
        return SUCCESS;
    }

    /**
     * 登录
     * @return
     */
    public String login() {
        System.out.println("name->" + name);
        System.out.println("password->" + password);
        logger.info(name);

        return SUCCESS;
    }
}
