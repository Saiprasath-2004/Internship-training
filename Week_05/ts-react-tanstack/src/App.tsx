import EmployeeCard from "./components/EmployeeCard";
import type { Employee } from "./types/employee";

export default function App() {

  const employees: Employee[] = [
    {
      id: 1,
      name: "Sai",
      role: "Frontend Developer",
      department: "Engineering",
      isActive: true,
    },
    {
      id: 2,
      name: "John",
      role: "Backend Developer",
      department: "Engineering",
      isActive: false,
    },
    {
      id: 3,
      name: "Priya",
      role: "UI Designer",
      department: "Design",
      isActive: true,
    },
  ]

  const handleView = (employee: Employee) => {
    alert(`${employee.name} - ${employee.role}`)
  }
 
  return (
    <>
      <div style={{padding: 20}}>
        {
          employees.map((employee) => (
            <EmployeeCard
                key={employee.id}
                employee={employee}
                onView={handleView}            
            />
        ))}
      </div>
     
    </>
  );
}
